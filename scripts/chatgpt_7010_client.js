// chatgpt_7010_client.js
// Client CDP exclusif pour la station d'audit GPT-6 de PSY7010
// Onglet dédié : "UQAM - PSY7010 - Audit station" (/c/6ab065ac)
// GARANTIE ANTI-COLLISION : Rejette formellement tout onglet PSY9613.

const fs = require('fs');

async function getChatGPTTab() {
    const res = await fetch('http://127.0.0.1:9223/json');
    const tabs = await res.json();
    
    // Recherche prioritaire par URL ou titre PSY7010
    let tab = tabs.find(t => t.type === 'page' && t.url && (t.url.includes('6ab065ac') || (t.url.includes('chatgpt.com') && t.title && t.title.includes('PSY7010'))));
    
    // Garde-fou strict anti-collision avec PSY9613
    if (tab && tab.title && tab.title.includes('PSY9613')) {
        throw new Error('ALERTE COLLISION : L\'onglet sélectionné appartient à PSY9613. Annulation immédiate.');
    }

    if (!tab) {
        throw new Error('Onglet ChatGPT UQAM - PSY7010 non trouvé sur le port 9223.');
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

function sendViaCDP(wsUrl, text) {
    return new Promise((resolve, reject) => {
        const ws = new WebSocket(wsUrl);
        const timeout = setTimeout(() => {
            ws.close();
            reject(new Error('Timeout sendViaCDP (30s)'));
        }, 30000);

        ws.onopen = () => {
            // Étape 1: focus sur le prompt-textarea
            ws.send(JSON.stringify({
                id: 1,
                method: 'Runtime.evaluate',
                params: {
                    expression: `(() => {
                        const el = document.querySelector('#prompt-textarea');
                        if (!el) return false;
                        el.focus();
                        return true;
                    })()`,
                    returnByValue: true
                }
            }));
        };

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.id === 1) {
                // Étape 2: insérer le texte via Input.insertText natif CDP
                ws.send(JSON.stringify({
                    id: 2,
                    method: 'Input.insertText',
                    params: { text: text }
                }));
            } else if (data.id === 2) {
                // Étape 3: cliquer sur envoyer
                setTimeout(() => {
                    ws.send(JSON.stringify({
                        id: 3,
                        method: 'Runtime.evaluate',
                        params: {
                            expression: `(() => {
                                const btn = document.querySelector('button[data-testid="send-button"], button[aria-label*="Send" i], button[aria-label*="Envoyer" i]');
                                if (!btn) return { error: 'Bouton d\\'envoi introuvable' };
                                const aria = btn.getAttribute('aria-disabled');
                                if (aria === 'true' || btn.disabled) {
                                    return { error: 'Bouton d\\'envoi désactivé', aria: aria };
                                }
                                btn.click();
                                return { success: true };
                            })()`,
                            returnByValue: true
                        }
                    }));
                }, 500);
            } else if (data.id === 3) {
                clearTimeout(timeout);
                ws.close();
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
    const tab = await getChatGPTTab();

    if (command === 'status') {
        const script = `
            (() => {
                const title = document.title;
                const textarea = document.querySelector('#prompt-textarea');
                const sendBtn = document.querySelector('button[data-testid="send-button"], button[aria-label*="Send" i], button[aria-label*="Envoyer" i]');
                const stopBtn = document.querySelector('button[data-testid="stop-button"], button[aria-label*="Stop" i], button[aria-label*="Arrêter" i]');
                const messages = Array.from(document.querySelectorAll('[data-message-author-role]'));
                const lastMsg = messages.length > 0 ? messages[messages.length - 1] : null;

                return {
                    tabId: "${tab.id}",
                    title: title,
                    url: window.location.href,
                    hasInput: !!textarea,
                    hasSendBtn: !!sendBtn,
                    sendBtnDisabled: sendBtn ? (sendBtn.disabled || sendBtn.getAttribute('aria-disabled') === 'true') : null,
                    isGenerating: !!stopBtn,
                    totalMessages: messages.length,
                    lastRole: lastMsg ? lastMsg.getAttribute('data-message-author-role') : null,
                    lastMessageSnippet: lastMsg ? lastMsg.innerText.substring(0, 300).replace(/\\n/g, ' ') : null
                };
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'read-last') {
        const script = `
            (() => {
                const assistantMessages = Array.from(document.querySelectorAll('[data-message-author-role="assistant"]'));
                if (assistantMessages.length === 0) return null;
                return assistantMessages[assistantMessages.length - 1].innerText;
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(res || '(Aucun message assistant)');
    } else if (command === 'inspect') {
        const script = `
            (() => {
                const turns = Array.from(document.querySelectorAll('[data-testid*="conversation-turn"]'));
                const stopBtn = document.querySelector('button[data-testid="stop-button"], button[aria-label*="Stop" i], button[aria-label*="Arrêter" i]');
                const sendBtn = document.querySelector('button[data-testid="send-button"], button[aria-label*="Send" i]');
                const allButtons = Array.from(document.querySelectorAll('button')).map(b => b.innerText || b.getAttribute('aria-label') || '').filter(Boolean);
                const lastTurn = turns.length > 0 ? turns[turns.length - 1] : null;
                const text = lastTurn ? lastTurn.innerText : '';
                return {
                    turnsCount: turns.length,
                    hasStopBtn: !!stopBtn,
                    hasSendBtn: !!sendBtn,
                    buttonsSnippet: allButtons.slice(-10),
                    textLength: text.length,
                    fullText: text
                };
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'dump') {
        const script = `
            (() => {
                const turns = Array.from(document.querySelectorAll('[data-testid*="conversation-turn"]'));
                const lastTurn = turns.length > 0 ? turns[turns.length - 1] : null;
                if (!lastTurn) return 'Aucun tour';
                const paragraphs = Array.from(lastTurn.querySelectorAll('p, h1, h2, h3, li')).map(p => p.innerText).filter(Boolean);
                const spin = lastTurn.querySelector('.animate-spin, [class*="spin"], [class*="loading"], [class*="pulse"]');
                return {
                    paragraphsCount: paragraphs.length,
                    firstParagraphs: paragraphs.slice(0, 5),
                    lastParagraphs: paragraphs.slice(-5),
                    hasSpinner: !!spin,
                    fullTextLength: lastTurn.innerText.length
                };
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'tools') {
        const script = `
            (() => {
                const turns = Array.from(document.querySelectorAll('[data-testid*="conversation-turn"]'));
                const lastTurn = turns.length > 0 ? turns[turns.length - 1] : null;
                if (!lastTurn) return 'Aucun tour';
                const buttons = Array.from(lastTurn.querySelectorAll('button')).map(b => ({
                    text: b.innerText,
                    aria: b.getAttribute('aria-label'),
                    expanded: b.getAttribute('aria-expanded')
                }));
                return buttons;
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        console.log(JSON.stringify(res, null, 2));
    } else if (command === 'save-last') {
        const targetPath = args[1];
        if (!targetPath) {
            console.error('Usage: node chatgpt_7010_client.js save-last "<chemin_fichier>"');
            process.exit(1);
        }
        const script = `
            (() => {
                const assistantMessages = Array.from(document.querySelectorAll('[data-message-author-role="assistant"]'));
                if (assistantMessages.length === 0) return null;
                return assistantMessages[assistantMessages.length - 1].innerText;
            })()
        `;
        const res = await evaluateInTab(tab.webSocketDebuggerUrl, script);
        if (res) {
            fs.writeFileSync(targetPath, res, 'utf8');
            console.log('Réponse GPT-6 sauvegardée (' + res.length + ' caractères) dans: ' + targetPath);
        } else {
            console.log('Aucune réponse à sauvegarder.');
        }
    } else if (command === 'send' || command === 'send-file') {
        let textToSend = '';
        if (command === 'send-file') {
            const filePath = args[1];
            if (!filePath || !fs.existsSync(filePath)) {
                console.error('Fichier introuvable:', filePath);
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

        const res = await sendViaCDP(tab.webSocketDebuggerUrl, textToSend);
        console.log(JSON.stringify(res, null, 2));
    }
}

main().catch(err => {
    console.error('Erreur:', err.message);
    process.exit(1);
});
