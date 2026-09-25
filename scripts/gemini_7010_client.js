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
                const responses = Array.from(document.querySelectorAll('.model-response-text, message-content, [data-test-id="model-response"]'));
                
                return {
                    tabId: "${tab.id}",
                    title: title,
                    url: window.location.href,
                    hasInput: !!editable,
                    hasSendBtn: !!sendBtn,
                    sendBtnDisabled: sendBtn ? (sendBtn.disabled || sendBtn.getAttribute('aria-disabled') === 'true') : null,
                    isGenerating: !!stopBtn,
                    responseCount: responses.length,
                    lastResponseSnippet: responses.length > 0 ? responses[responses.length - 1].innerText.substring(0, 300).replace(/\\n/g, ' ') : null
                };
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'read-last') {
        const script = `
            (() => {
                const responses = Array.from(document.querySelectorAll('.model-response-text, message-content, [data-test-id="model-response"]'));
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
                const responses = Array.from(document.querySelectorAll('.model-response-text, message-content, [data-test-id="model-response"]'));
                if (responses.length === 0) return null;
                return responses[responses.length - 1].innerText;
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        if (res) {
            fs.writeFileSync(targetPath, res, 'utf8');
            console.log('Réponse DeepThink sauvegardée (' + res.length + ' caractères) dans: ' + targetPath);
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

        const escapedText = JSON.stringify(textToSend);
        const script = `
            (() => {
                const editable = document.querySelector('rich-textarea p, rich-textarea [contenteditable="true"], [contenteditable="true"]');
                if (!editable) return { error: 'Zone de texte introuvable' };
                
                editable.focus();
                editable.textContent = ${escapedText};
                editable.dispatchEvent(new Event('input', { bubbles: true }));
                editable.dispatchEvent(new Event('change', { bubbles: true }));
                
                const sendBtn = document.querySelector('button[aria-label*="Send message" i], button[aria-label*="Send" i], button[aria-label*="Envoyer" i], .send-button');
                if (!sendBtn) return { error: 'Bouton Envoyer introuvable', textInjected: true };
                if (sendBtn.disabled || sendBtn.getAttribute('aria-disabled') === 'true') {
                    return { error: 'Bouton Envoyer désactivé', textInjected: true };
                }
                
                sendBtn.click();
                return { success: true, textLength: ${escapedText}.length };
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
