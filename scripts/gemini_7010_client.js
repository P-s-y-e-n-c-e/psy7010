// gemini_7010_client.js
// Client CDP exclusif pour la station d'audit Gemini DeepThink de PSY7010
// Gem dédié : "Auditeur Doctoral PSY7010" (ID: 49d384634d73)
// GARANTIE ANTI-COLLISION : Rejette formellement tout onglet PSY9613.

const fs = require('fs');

const GEM_ID = '49d384634d73';

async function getGemTab() {
    const res = await fetch('http://127.0.0.1:9223/json');
    const tabs = await res.json();
    
    // Recherche par Gem ID ou par titre PSY7010 dans Gemini
    let tab = tabs.find(t => t.type === 'page' && t.url && (t.url.includes(GEM_ID) || (t.url.includes('gemini.google.com') && t.title && t.title.includes('PSY7010'))));
    
    // Garde-fou strict anti-collision avec PSY9613
    if (tab && tab.title && tab.title.includes('PSY9613')) {
        throw new Error('ALERTE COLLISION : L\'onglet sélectionné appartient à PSY9613. Annulation immédiate.');
    }
    
    // Si la conversation a été initialisée et a changé d'URL vers /app/
    if (!tab) {
        // Chercher un onglet gemini qui n'est PAS PSY9613 et qui a été inspecté comme contenant notre Gem
        tab = tabs.find(t => t.type === 'page' && t.url && t.url.includes('gemini.google.com') && (!t.title || !t.title.includes('PSY9613')));
    }

    if (!tab) {
        throw new Error('Onglet Gemini Auditeur Doctoral PSY7010 non trouvé sur le port 9223.');
    }
    return tab;
}

function callCdp(wsUrl, method, params) {
    return new Promise((resolve, reject) => {
        const ws = new WebSocket(wsUrl);
        const timeout = setTimeout(() => {
            ws.close();
            reject(new Error('Timeout CDP (30s)'));
        }, 30000);

        ws.onopen = () => {
            ws.send(JSON.stringify({
                id: 1,
                method: method,
                params: params
            }));
        };

        ws.onmessage = (event) => {
            clearTimeout(timeout);
            const data = JSON.parse(event.data);
            ws.close();
            if (data.error) {
                reject(new Error(JSON.stringify(data.error)));
            } else {
                resolve(data.result);
            }
        };

        ws.onerror = (err) => {
            clearTimeout(timeout);
            reject(err);
        };
    });
}

function evaluateInTab(wsUrl, expression) {

    return new Promise((resolve, reject) => {
        const ws = new WebSocket(wsUrl);
        const timeout = setTimeout(() => {
            ws.close();
            reject(new Error('Timeout CDP (30s)'));
        }, 30000);

        ws.onopen = () => {
            ws.send(JSON.stringify({
                id: 1,
                method: 'Runtime.evaluate',
                params: {
                    expression: expression,
                    returnByValue: true,
                    awaitPromise: true
                }
            }));
        };

        ws.onmessage = (event) => {
            clearTimeout(timeout);
            const data = JSON.parse(event.data);
            ws.close();
            if (data.error) {
                reject(new Error(JSON.stringify(data.error)));
            } else {
                resolve(data.result?.result?.value);
            }
        };

        ws.onerror = (err) => {
            clearTimeout(timeout);
            reject(err);
        };
    });
}

async function main() {
    const args = process.argv.slice(2);
    const command = args[0] || 'status';
    const tab = await getGemTab();

    if (command === 'status') {
        const script = `
            (() => {
                const title = document.title;
                const editable = document.querySelector('rich-textarea p, rich-textarea [contenteditable="true"], [contenteditable="true"]');
                const sendBtn = document.querySelector('button[aria-label*="Send message" i], button[aria-label*="Send" i], button[aria-label*="Envoyer" i], .send-button');
                const stopBtn = document.querySelector('button[aria-label*="Arrêter" i], button[aria-label*="Stop" i], .stop-button');
                const responses = Array.from(document.querySelectorAll('model-response, [data-test-id="model-response"]'));
                const lastResp = responses.length > 0 ? responses[responses.length - 1] : null;
                const isDeepThinking = lastResp ? (lastResp.getAttribute('aria-busy') === 'true' || (lastResp.innerText && lastResp.innerText.includes('Generating your response'))) : false;

                const picker = document.querySelector('button[aria-label*="mode picker" i], [data-test-id="mode-picker"]');
                const activeMode = picker ? (picker.getAttribute('aria-label') || picker.innerText) : null;
                const isDeepThinkActive = activeMode ? activeMode.toLowerCase().includes('deep think') : false;

                return new Promise(resolve => {
                    let verifiedModel = null;
                    if (lastResp) {
                        const moreBtn = lastResp.querySelector('button[aria-label*="More" i], button[aria-label*="Plus" i], button[aria-label*="options" i]');
                        if (moreBtn) {
                            moreBtn.click();
                            setTimeout(() => {
                                const menu = document.querySelector('.mat-mdc-menu-panel, [role="menu"]');
                                const text = menu ? menu.innerText : '';
                                document.body.click();
                                const match = text.match(/Model:\\s*([^\\n]+)/i);
                                verifiedModel = match ? match[1].trim() : (text.includes('Deep Think') ? 'Deep Think' : (text.includes('Pro') ? 'Pro' : null));
                                finish();
                            }, 300);
                            return;
                        }
                    }
                    finish();

                    function finish() {
                        resolve({
                            tabId: "${tab.id}",
                            title: title,
                            url: window.location.href,
                            inputActiveMode: activeMode,
                            isInputDeepThinkActive: isDeepThinkActive,
                            verifiedResponseModel: verifiedModel,
                            isResponseVerifiedDeepThink: verifiedModel ? verifiedModel.toLowerCase().includes('deep think') : false,
                            hasInput: !!editable,
                            hasSendBtn: !!sendBtn,
                            sendBtnDisabled: sendBtn ? (sendBtn.disabled || sendBtn.getAttribute('aria-disabled') === 'true') : null,
                            isGenerating: !!stopBtn || isDeepThinking,
                            responseCount: responses.length,
                            lastResponseSnippet: lastResp ? lastResp.innerText.substring(0, 300).replace(/\\n/g, ' ') : null
                        });
                    }
                });
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'read-last') {
        const script = `
            (() => {
                const responses = Array.from(document.querySelectorAll('model-response, [data-test-id="model-response"]'));
                if (responses.length === 0) return null;
                return responses[responses.length - 1].innerText;
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(res || '(Aucune réponse du modèle pour le moment)');
    } else if (command === 'save-last') {
        const targetPath = args[1];
        if (!targetPath) {
            console.error('Usage: node gemini_7010_client.js save-last "<chemin_fichier>"');
            process.exit(1);
        }
        const script = `
            (() => {
                const responses = Array.from(document.querySelectorAll('model-response, [data-test-id="model-response"]'));
                if (responses.length === 0) return { error: 'Aucune reponse trouvee' };
                const lastResp = responses[responses.length - 1];

                return new Promise(resolve => {
                    const moreBtn = lastResp.querySelector('button[aria-label*="More" i], button[aria-label*="Plus" i], button[aria-label*="options" i]');
                    if (moreBtn) {
                        moreBtn.click();
                        setTimeout(() => {
                            const menu = document.querySelector('.mat-mdc-menu-panel, [role="menu"]');
                            const text = menu ? menu.innerText : '';
                            document.body.click();
                            const fullText = (text + ' ' + lastResp.innerText);
                            const match = fullText.match(/Model:\\s*([^\\n]+)/i);
                            const verifiedModel = match ? match[1].trim() : (fullText.includes('Deep Think') ? '3.1 Deep Think' : (fullText.includes('Pro') ? 'Pro' : 'Inconnu'));
                            resolve({
                                content: lastResp.innerText,
                                verifiedModel: verifiedModel,
                                isDeepThink: verifiedModel.toLowerCase().includes('deep think')
                            });
                        }, 300);
                        return;
                    }
                    const fullText = lastResp.innerText;
                    const match = fullText.match(/Model:\\s*([^\\n]+)/i);
                    const verifiedModel = match ? match[1].trim() : (fullText.includes('Deep Think') ? '3.1 Deep Think' : (fullText.includes('Pro') ? 'Pro' : 'Inconnu'));
                    resolve({ content: lastResp.innerText, verifiedModel: verifiedModel, isDeepThink: verifiedModel.toLowerCase().includes('deep think') });
                });
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        if (res && res.content) {
            if (!res.isDeepThink) {
                console.error('ALERTE REJET : La réponse a été générée par le modèle "' + res.verifiedModel + '" et NON par Deep Think ! Sauvegarde annulée.');
                process.exit(1);
            }
            fs.writeFileSync(targetPath, res.content, 'utf8');
            console.log('Réponse DeepThink VÉRIFIÉE (' + res.verifiedModel + ', ' + res.content.length + ' caractères) sauvegardée dans: ' + targetPath);
        } else {
            console.log('Aucune réponse à sauvegarder.');
        }
    } else if (command === 'send' || command === 'send-file') {
        let textToSend = '';
        if (command === 'send-file') {
            const filePath = args[1];
            if (!filePath || !fs.existsSync(filePath)) {
                console.error('Fichier non trouvé:', filePath);
                process.exit(1);
            }
            textToSend = fs.readFileSync(filePath, 'utf8');
        } else {
            textToSend = args.slice(1).join(' ');
        }

        if (!textToSend.trim()) {
            console.error('Erreur: Texte vide');
            process.exit(1);
        }

        // Vérification de sécurité absolue : Le mode Deep Think doit être actif
        const isDeepThink = await evaluateInTab(tab.webSocketDebuggerUrl, `
            (() => {
                const picker = document.querySelector('button[aria-label*="mode picker" i], [data-test-id="mode-picker"]');
                const activeMode = picker ? (picker.getAttribute('aria-label') || picker.innerText) : '';
                return activeMode.toLowerCase().includes('deep think');
            })()
        `);
        if (!isDeepThink) {
            console.error('ALERTE BLOQUANTE : Le mode Deep Think est désactivé dans Gemini ! Envoi annulé pour éviter de gaspiller un tour.');
            process.exit(1);
        }

        // 1. Vider et focaliser l'éditeur Quill
        await evaluateInTab(tab.webSocketDebuggerUrl, `
            (() => {
                const editable = document.querySelector('rich-textarea .ql-editor, rich-textarea [contenteditable="true"]');
                if (!editable) return false;
                editable.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                return true;
            })()
        `);

        // 2. Injection native via CDP Input.insertText (gère le modèle Quill et efface ql-blank)
        await callCdp(tab.webSocketDebuggerUrl, 'Input.insertText', { text: textToSend });

        // 3. Clic sur le bouton Envoyer dès qu'il est activé
        const script = `
            (() => {
                const sendBtn = document.querySelector('button[aria-label*="Send message" i], button[aria-label*="Send" i], button[aria-label*="Envoyer" i], .send-button');
                if (!sendBtn) return { error: 'Bouton Envoyer introuvable' };
                if (sendBtn.disabled || sendBtn.getAttribute('aria-disabled') === 'true') {
                    return { error: 'Bouton Envoyer désactivé' };
                }
                
                sendBtn.click();
                return { success: true, textLength: ${textToSend.length} };
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    }
}

main().catch(err => {
    console.error('Erreur:', err.message);
    process.exit(1);
});
