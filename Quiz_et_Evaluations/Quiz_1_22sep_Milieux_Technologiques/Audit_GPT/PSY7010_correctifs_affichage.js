// Remplacements à effectuer dans le code existant (pas un script à ajouter tel quel).
// showFeedback(q, selectedIdx) :
document.getElementById('fbExplanation').innerHTML =
  '<strong>Explication théorique :</strong> ' + (q.doc_explanation || '');
document.getElementById('fbExamTipText').textContent = q.exam_tip || '';
document.getElementById('fbDocQuote').textContent = q.doc_quote || '';

// Fonction d’affichage des cartes :
document.getElementById('fcExplanationText').innerHTML =
  '<strong>Synthèse :</strong> ' + (q.doc_explanation || '');
document.getElementById('fcExamTipText').innerHTML =
  '<strong>💡 Astuce examen :</strong> ' + (q.exam_tip || '');
document.getElementById('fcSourceQuoteText').textContent =
  (q.doc_quote || '') + (q.doc_page ? ' (' + q.doc_page + ')' : '');

// Ne jamais rééquilibrer les lettres en changeant correctIndex seul.
// Toute permutation doit déplacer ensemble : option, rétroaction, index correct,
// index de réponse sauvegardé (ou réinitialiser les anciennes sauvegardes).
