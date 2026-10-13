# -*- coding: utf-8 -*-
"""
Générateur de la traduction française intégrale et des viewports bilingues
pour Congiu & Moscati (2022) — Revue Critique des Nudges.
"""

import re

def get_congiu_full_translation():
    return """# Congiu, R., & Moscati, I. (2022) — Revue Critique des Nudges : Définitions, Justifications et Efficacité

**Titre original :** *A review of nudges: Definitions, justifications, effectiveness*  
**Revue :** *Journal of Economic Surveys*, Volume 36, Numéro 1, Année 2022, pp. 188–213.  
**DOI :** `https://doi.org/10.1111/joes.12453`  
**Auteurs :** Luca Congiu (Département d'économie, Université d'Insubrie & Université Bocconi) et Ivan Moscati (Département d'économie, Université d'Insubrie & Centre de philosophie des sciences naturelles et sociales, London School of Economics).  
**Licence :** Open Access Creative Commons Attribution CC BY 4.0.  
**Cadre académique :** PSY7010 — Sciences psychologiques appliquées : Commerce et consommation 1 (Guillaume Beaulac & Mario Passalacqua, UQAM).

---

## 📋 Fiche de Synthèse Préalable & Points Clés
* **Statut académique :** Lecture obligatoire fondamentale — Séance 06 (Quiz 2).
* **Les 3 dimensions analysées par la revue :**
  1. **Définition exacte du Nudge :** De la définition quadripartite de Thaler & Sunstein (2008) aux reformulations de Hansen (2016) et Sunstein (2014, 2017).
  2. **Justification philosophique :** Le paternalisme libertarien, ses apories épistémiques (comment l'architecte du choix connaît-il les vraies préférences de l'agent ?) et les risques d'atteinte à l'autonomie décisionnelle (manipulation et opacité).
  3. **Efficacité empirique & Nudges vs Boosts :** Efficacité à court vs long terme, comparaison avec les instruments fiscaux et réglementaires classiques, et distinction théorique majeure avec les *boosts* cognitifs (Hertwig & Grüne-Yanoff, 2017).

---

### [Page 188]

#### RÉSUMÉ
En 2008, l'économiste comportemental Richard Thaler et le juriste Cass Sunstein ont publié un ouvrage dans lequel ils préconisaient une approche novatrice des politiques publiques fondée sur la notion de « nudge » (coup de pouce). En substance, un nudge est une intervention dans le contexte décisionnel qui oriente les décisions des individus en agissant sur leurs biais cognitifs. La notion de nudge a suscité un débat intense à travers différentes disciplines et a rencontré un vif succès auprès de nombreux décideurs publics dans le monde. Cet article passe en revue les débats et les recherches sur les nudges en se concentrant sur trois dimensions principales : (1) la définition exacte des nudges ; (2) la justification des politiques de nudge, avec une attention particulière au « paternalisme libertarien » ; et (3) l'efficacité des nudges, tant dans la durée qu'en comparaison avec les politiques publiques traditionnelles.

**Mots-clés :** Économie du bien-être comportementale, boosts, rationalité limitée, paternalisme libertarien, nudge.

---

### 1. INTRODUCTION

#### 1.1. Mise en contexte
Les modèles de prise de décision individuelle qui ont dominé la science économique jusqu'à la fin du XXe siècle — regroupés sous l'appellation générique d'économie néoclassique — reposent sur l'hypothèse de l'agent rationnel (*Homo Economicus*). Ce modèle postule que les individus disposent d'un ensemble complet et transitif de préférences bien ordonnées, qu'ils traitent l'ensemble des informations disponibles de façon bayésienne et sans faille, et qu'ils choisissent systématiquement l'action qui maximise leur utilité espérée sous contrainte budgétaire.

À partir des années 1970, les travaux pionniers de la psychologie cognitive et de l'économie comportementale (notamment Daniel Kahneman, Amos Tversky et Herbert Simon) ont mis en lumière une série impressionnante d'anomalies comportementales et de déviations systématiques par rapport aux prédictions du modèle néoclassique. Il a été démontré que les décideurs réels recourent à des heuristiques de jugement qui conduisent à des biais cognitifs (tels que l'aversion aux pertes, l'ancrage, le biais de confirmation, l'heuristique de disponibilité ou le biais de statu quo) et que leurs choix dépendent de manière critique de l'architecture du choix, c'est-à-dire de la façon dont les options sont présentées, étiquetées et ordonnées dans l'environnement décisionnel.

---

### [Page 189]

Face à ces constats, deux attitudes ont émergé chez les économistes. Une partie des chercheurs a considéré que ces biais constituaient des failles de rationalité justifiant une intervention corrective de l'État pour protéger les individus contre leurs propres erreurs de calcul. Toutefois, les instruments traditionnels de l'action publique — la régulation par l'interdiction/obligation juridique et la fiscalité par taxes ou subventions financières — présentent des coûts économiques élevés et restreignent la liberté de choix des citoyens.

C'est dans ce contexte que Richard Thaler et Cass Sunstein (2008) ont proposé une troisième voie séduisante : le **nudge**. En modifiant subtilement l'architecture du choix sans interdire aucune option ni modifier significativement les incitations économiques, il devient possible d'orienter les comportements vers des issues jugées bénéfiques pour les décideurs eux-mêmes (*pro-self nudges*) ou pour la société dans son ensemble (*pro-social nudges*).

#### 1.2. Plan de l'article
La présente revue critique s'articule autour de trois volets :
1. **La question définitionnelle (Sections 2 à 4) :** Examen minutieux de la définition originale de 2008, analyse des difficultés conceptuelles qu'elle soulève, passage en revue des définitions alternatives (Hansen, Sunstein, Hausman & Welch) et présentation des taxinomies comportementales.
2. **La question de la justification politique et philosophique (Sections 5 à 7) :** Analyse du concept de paternalisme libertarien, confrontation aux objections éthiques portant sur l'autonomie et la manipulation, et étude des justifications alternatives fondées sur l'acceptabilité publique.
3. **La question de l'efficacité empirique (Sections 8 et 9) :** Comparaison des nudges avec le paradigme concurrent des « boosts » (Hertwig & Grüne-Yanoff), évaluation de la pérennité temporelle des effets, de la taille des effets réels et des risques de substitution (*crowding-out*) face aux politiques publiques structurelles.

---

### [Page 190]

### 2. LA DÉFINITION ORIGINALE DU NUDGE ET SES PROBLÈMES CONCEPTUELS

Dans leur ouvrage séminal de 2008, Thaler et Sunstein définissent le nudge à travers une proposition célèbre mais complexe, énoncée aux pages 6 et 8.

```text
« Un coup de pouce (nudge) est tout aspect de l'architecture du choix qui modifie le comportement des personnes d'une manière prévisible sans [1] interdire aucune option ni [2] modifier de façon significative leurs incitations économiques. Pour être considéré comme un simple coup de pouce, l'intervention doit être [3] facile et peu coûteuse à éviter. De surcroît, un nudge [4] modifie significativement le comportement des Humains [les agents réels à rationalité limitée], tout en étant ignoré par les Écons [les agents parfaitement rationnels de la théorie néoclassique]. »
— Thaler & Sunstein (2008, pp. 6 et 8)
```

Cette définition originale s'avère être une définition quadripartite exigeante qui combine quatre critères cumulatifs :
1. **Critère de liberté de choix :** Aucune option matérielle ou juridique ne doit être exclue du menu décisionnel de l'agent.
2. **Critère de neutralité financière :** Les incitations monétaires et économiques fondamentales ne doivent pas être altérées de façon substantielle.
3. **Critère de contournement aisé (*cheap and easy to avoid*) :** Si l'individu souhaite refuser l'orientation suggérée, le coût de sortie (en temps, en argent ou en effort cognitif) doit être quasi nul.
4. **Critère de sélectivité cognitive :** L'intervention n'agit que sur les failles ou biais des agents humains imparfaits ; un agent néoclassique parfaitement informé et rationnel (*Econ*) calculerait son optimum sans être influencé par la disposition spatiale ou le cadrage.

---

### [Page 191]

#### 2.1. L'ajout d'options et l'effet leurre (*Decoy Effect*)
Le critère « sans interdire aucune option » stipule qu'une politique de nudge ne peut restreindre l'ensemble des choix accessibles à l'agent. Cependant, la définition de 2008 demeure muette sur la question inverse : une intervention qui **augmente** l'ensemble des options disponibles peut-elle constituer un nudge ?

L'analyse de l'effet leurre (*decoy effect*, ou attraction asymétrique théorisée par Huber, Payne et Puto, 1982) apporte un éclairage décisif. Supposons qu'un consommateur hésite entre deux options : 
- Option A : un abonnement numérique seul à 50 $.
- Option B : un abonnement papier + numérique à 125 $.

L'architecte du choix introduit alors une troisième option dominée C (le « leurre ») : 
- Option C : un abonnement papier seul à 125 $.

L'option C est asymétriquement dominée par l'option B (pour le même prix de 125 $, B offre le papier ET le numérique, alors que C n'offre que le papier). L'introduction de C fait bondir la proportion d'usagers choisissant l'option B.

Selon la définition originale de Thaler et Sunstein (2008), **l'effet leurre est un nudge authentique** :
1. Aucune option préexistante n'a été retirée ou interdite (l'ensemble des choix a été élargi).
2. Les prix et incitatifs des options A et B sont restés strictement identiques.
3. Le consommateur peut éviter le leurre à coût nul en continuant d'opter pour A ou B.
4. Un agent parfaitement rationnel (*Econ*) ignorerait purement et simplement l'option C dominée et son choix entre A et B ne serait en rien modifié. Seuls les agents humains à rationalité limitée révisent leur préférence en raison du contraste perceptuel créé par le leurre.

Toutefois, comme le soulignent Congiu et Moscati, bien que l'effet leurre satisfasse mot à mot la définition de 2008, il s'écarte radicalement de l'esprit du « paternalisme libertarien » car il est fréquemment employé par des firmes commerciales à des fins de maximisation du profit aux dépens de l'usager (*dark pattern*).

---

### [Page 192]

#### 2.2. Au-delà des incitations économiques : le cas de la taxe de 5 sous sur les sacs d'épicerie
Le deuxième critère de la définition de 2008 exige que l'intervention ne modifie pas significativement les incitations économiques de l'agent. Que se passe-t-il lorsque l'intervention introduit un coût monétaire minime ?

Le cas classique analysé dans la littérature est celui de la taxe de 5 sous (0,05 $) imposée sur les sacs d'épicerie jetables en plastique. 
- Du point de vue de l'économie néoclassique, une variation de 5 sous sur un panier d'épicerie de 100 $ représente un changement financier infinitésimal (0,05 %) qui ne devrait avoir quasiment aucun impact sur la consommation.
- Pourtant, sur le terrain empirique, l'instauration de cette taxe de 5 sous a entraîné un effondrement immédiat de plus de 80 % de l'usage des sacs plastiques (Homonoff, 2018).

Ce résultat s'explique par l'**aversion aux pertes** : prélever 5 sous est encodé par l'esprit humain comme une perte financière directe, ce qui déclenche une réaction psychologique disproportionnée par rapport à un rabais équivalent de 5 sous offert aux clients apportant leur propre sac réutilisable.

Or, sur le plan de la classification académique, ce cas engendre une contradiction majeure :
- **Selon la définition originale de Thaler et Sunstein (2008) :** La taxe de 5 sous **n'est pas un nudge**. Elle modifie formellement une incitation financière (elle instaure un prix là où l'article était gratuit) et elle ne serait pas totalement ignorée par un Econ qui calcule son budget.
- **Selon la définition de Hansen (2016) :** La taxe de 5 sous **est un nudge**. Dès lors que l'ampleur spectaculaire du changement de comportement ne découle pas du signal-prix économique en soi, mais de l'exploitation d'un biais psychologique sous-jacent (le point de référence et l'aversion aux pertes), Hansen considère que ce mécanisme transforme la taxe en nudge.

---

### [Page 193]

#### 2.3. Transparence, coûts cognitifs et facilité d'évitement
Le troisième critère impose que le nudge soit « facile et peu coûteux à éviter » (*cheap and easy to avoid*). Thaler et Sunstein précisent en note de bas de page que les coûts d'évitement ne sont pas seulement matériels ou pécuniaires, mais également cognitifs et attentionnels.

Si le refus d'une option suggérée requiert de remplir des formulaires administratifs complexes, de déchiffrer des avertissements en petits caractères ou de surmonter une forte culpabilité sociale, le coût d'évitement devient psychologiquement élevé. Dans ces configurations, l'intervention cesse d'être un simple coup de pouce bienveillant et s'apparente à une contrainte déguisée (*sludge*).

#### 2.4. Canaux d'influence : processus rationnels ou défaillances de rationalité ?
Le quatrième critère stipule que les nudges influencent les Humains tout en étant ignorés par les Écons. Cela signifie qu'un nudge opère nécessairement en prenant appui sur les limites cognitives, les heuristiques ou les biais décisionnels des individus.

Toutefois, certaines interventions populaires étiquetées comme des nudges — par exemple fournir une information factuelle claire sur un GPS ou afficher le nombre de calories sur un menu — s'adressent directement à la délibération rationnelle de l'agent. Un agent parfaitement rationnel tiendrait compte de cette information nouvelle pour réévaluer son calcul d'utilité. Ces interventions relèvent-elles alors du nudge ou de l'éducation informationnelle classique ? Cette ambiguïté a contraint les théoriciens à formuler des définitions révisées.

---

### [Page 194]

### 3. DÉFINITIONS RÉVISÉES DU NUDGE

Pour pallier les apories de la formulation originale de 2008, deux révisions majeures ont été proposées dans la littérature.

#### 3.1. La définition de Hansen (2016) : le recentrage sur les failles de rationalité
Pelle Guldborg Hansen (2016) propose d'épurer la définition en abandonnant les clauses confuses sur les incitations financières pour ancrer formellement le nudge dans la psychologie cognitive :

```text
« Une intervention dans l'architecture du choix constitue un nudge si et seulement si son efficacité comportementale repose sur l'exploitation des limites cognitives, des heuristiques ou des biais des décideurs, sans restreindre formellement l'éventail des choix. »
— Hansen (2016)
```

Selon Hansen :
1. Une campagne fournissant une information purement factuelle, transparente et destinée à la réflexion critique n'est pas un nudge.
2. En revanche, toute modification du contexte exploitant un ancrage, une saillance visuelle, un cadrage ou une option par défaut constitue un nudge, même si elle s'accompagne d'incitations monétaires mineures (comme la taxe de 5 sous).

#### 3.2. La définition de Sunstein au sens large (2014, 2017)
À l'inverse d'Hansen qui resserre la définition, Cass Sunstein a défendu une définition inclusive du nudge au sens large (*broad sense*) :

```text
« Un nudge au sens large englobe toute intervention dans l'architecture du choix qui préserve la liberté décisionnelle, qu'elle agisse par des mécanismes cognitifs automatiques (Système 1) ou qu'elle fournisse des informations éducatives et réflexives destinées à éclairer la délibération consciente (Système 2). »
— Sunstein (2014, 2017)
```

Pour Sunstein, un rappel calendaire, un panneau d'affichage clair ou un calculateur d'itinéraire constituent d'authentiques nudges parce qu'ils aident les individus à faire de meilleurs choix selon leur propre jugement, sans recourir à la coercition.

---

### [Page 195]

### 4. TAXINOMIES DES NUDGES

#### 4.1. La taxinomie quadripartite de Hansen et Jespersen (2013)
L'une des classifications les plus rigoureuses et les plus influentes est la matrice développée par Hansen et Jespersen (2013), structurée selon deux axes orthogonaux :
1. **L'axe du mode cognitif sollicité :**
   - **Système 1 (Automatique) :** L'intervention sollicite des processus mentaux rapides, implicites, émotionnels et peu gourmands en mémoire de travail.
   - **Système 2 (Réflexif) :** L'intervention sollicite la délibération consciente, le calcul explicite, l'évaluation critique et la mémoire de travail.
2. **L'axe du degré de transparence :**
   - **Transparent :** L'intention de l'architecte du choix et le mécanisme d'influence sont manifestes et facilement identifiables par le décideur.
   - **Opaque :** L'intention ou le mécanisme d'influence ne sont pas discernables par le décideur au moment du choix, qui ignore que son comportement est dirigé.

---

### [Page 196]

Le croisement de ces deux dimensions produit **quatre quadrants de nudges** :

| Mode cognitif \ Transparence | **Transparent** | **Opaque** |
|---|---|---|
| **Système 2 (Réflexif)** | **Type 2 Transparent :** Lettre détaillée invitant à comparer explicitement sa consommation énergétique à celle de pairs comparables ; avertissements sanitaires textuels circonstanciés. | **Type 2 Opaque :** Cadrage subtil de questions dans une enquête orientant la délibération sans que l'enquêté s'en aperçoive. |
| **Système 1 (Automatique)** | **Type 1 Transparent :** Empreintes de pas peintes au sol guidant visiblement vers les escaliers plutôt que l'escalier mécanique ; icône de cœur apposée sur les plats sains. | **Type 1 Opaque :** Mouche gravée au fond de l'urinoir stimulant un réflexe de visée automatique ; assiettes de taille réduite dans un buffet pour induire une satiété précoce. |

#### Exemples emblématiques :
- **La mouche dans l'urinoir (Schiphol, Amsterdam) :** L'intervention s'adresse exclusivement à une réponse motrice automatique déclenchée par un repère perceptif (Système 1), sans modifier les incitatifs économiques ni imposer de contrainte. L'usager ne délibère pas consciemment sur l'hygiène de la pièce ; il s'agit d'un nudge de Type 1 automatique.
- **Les options par défaut (*Default Rules*) :** Lorsqu'un individu est confronté à un choix complexe pour lequel ses préférences ne sont pas arrêtées ou dont l'analyse requiert des compétences de calcul qu'il ne maîtrise pas, il a tendance à conserver l'option précochée par défaut. Ce comportement s'explique par la combinaison de la paresse cognitive, du biais de statu quo et de l'inférence implicite que l'option par défaut représente la recommandation légitime de l'autorité.

---

### [Page 197]

#### 4.2. Nudges Pro-Self vs Nudges Pro-Social
Une autre distinction fondamentale porte sur le bénéficiaire de l'intervention :
- **Nudges pro-self :** Conçus pour améliorer le bien-être direct du décideur lui-même (ex. régimes d'épargne-retraite SMarT, alimentation équilibrée, exercice physique).
- **Nudges pro-social :** Conçus pour générer des externalités positives ou préserver des biens publics partagés au bénéfice de la collectivité (ex. don d'organes, réduction de la consommation électrique, tri des déchets, ponctualité fiscale).

---

### [Page 198]

### 5. LA JUSTIFICATION PHILOSOPHIQUE DU PATERNALISME LIBERTARIEN

Pour Thaler et Sunstein, le cadre conceptuel qui légitime l'usage des nudges par les institutions publiques et privées est le **paternalisme libertarien**.
- **La composante libertarienne :** Préserver scrupuleusement la liberté de choix. Aucune option légale n'est interdite et le citoyen conserve la possibilité permanente de refuser l'option préconisée.
- **La composante paternaliste :** Autoriser les architectes du choix à structurer le contexte décisionnel de façon délibérée afin d'orienter les citoyens vers les choix qui maximiseront leur propre bien-être, tel qu'ils le jugeraient eux-mêmes s'ils disposaient d'une information complète et d'une rationalité parfaite.

Thaler et Sunstein avancent un argument central : **l'architecture du choix est inévitable**. Dès lors qu'une autorité conçoit un formulaire, dispose des aliments sur un comptoir ou rédige un contrat, elle doit obligatoirement choisir un ordre d'apparition et une option par défaut. Puisqu'une architecture neutre n'existe pas dans le monde réel, il est selon eux préférable et moralement responsable d'agencer intentionnellement cette architecture pour favoriser le bien-être des personnes plutôt que de la laisser au hasard ou aux intérêts commerciaux.

---

### [Page 199]

### 6. LES OBJECTIONS CRITIQUES AU PATERNALISME LIBERTARIEN

En dépit de son attractivité apparente, la doctrine du paternalisme libertarien a essuyé des critiques philosophiques et méthodologiques profondes.

#### 6.1. Le problème épistémique de l'architecte du choix
Comment l'architecte du choix sait-il avec certitude ce qui constitue le « bien-être » du décideur ? L'économie néoclassique déduisait les préférences des choix observés sur le marché (théorie des préférences révélées). Si l'économie comportementale démontre que les choix réels sont pollués par des biais cognitifs et des effets d'agencement, les préférences révélées s'effondrent. 

L'autorité publique se retrouve alors contrainte de postuler arbitrairement ce que devraient être les « véritables préférences » des citoyens (par exemple : « tout le monde devrait épargner davantage » ou « tout le monde devrait consommer moins de calories »), ce qui ouvre la voie à un paternalisme d'État traditionnel autoritaire.

---

### [Page 200]

#### 6.2. Le problème de l'autonomie et de la manipulation décisionnelle
La critique éthique la plus redoutable (formulée notamment par Hausman et Welch, 2010, ainsi que par Bovens, 2009) attaque le cœur du dispositif : **la subversion de l'autonomie rationnelle**.

Même si toutes les options matérielles restent juridiquement accessibles sur le papier, un nudge qui exploite des heuristiques opaques et contourne la réflexion consciente prive l'individu de son statut d'agent autonome capable de peser ses propres motifs d'action. En manipulant l'environnement perceptif pour faire pencher la balance décisionnelle à l'insu de la personne, l'État ne traite plus le citoyen comme un être doué de raison, mais comme un système réactif dont on pilote les réflexes. Lorsque cette influence s'exerce de façon opaque (comme dans les nudges de Type 1 opaques), la liberté formelle de choix devient une illusion théorique.

---

### [Page 201]

### 7. JUSTIFICATIONS DES NUDGES AU-DELÀ DU PATERNALISME LIBERTARIEN

Face aux impasses du paternalisme libertarien, plusieurs auteurs ont tenté de refonder la légitimité des nudges sur d'autres bases normatives :
1. **Les justifications démocratiques et procédurales :** Soumettre les nudges publics à un débat parlementaire transparent et à un contrôle citoyen régulier.
2. **Le critère d'acceptabilité publique :** Plusieurs enquêtes empiriques internationales démontrent que les citoyens soutiennent massivement les nudges transparents visant des objectifs de santé ou de sécurité, mais rejettent les interventions opaques ou celles soupçonnées de servir des intérêts politiques partisans.

---

### [Page 202]

### 8. NUDGES VERSUS BOOSTS : LE GRAND DÉBAT THÉORIQUE

En opposition féconde aux partisans du nudge, un courant de chercheurs en psychologie cognitive conduit par Ralph Hertwig et Till Grüne-Yanoff (2017) a développé le paradigme alternatif des **« boosts »** (amplificateurs de compétences).

La divergence entre Nudges et Boosts constitue une ligne de démarcation théorique majeure en sciences psychologiques appliquées :

```text
« Tandis que les nudges modifient l'environnement immédiat pour orienter le comportement d'individus dont les compétences cognitives restent inchangées, les boosts développent, enrichissent et outillent directement les compétences décisionnelles des personnes afin de leur permettre d'exercer un choix autonome éclairé. »
— Hertwig & Grüne-Yanoff (2017)
```

---

### [Page 203]

#### Comparaison systématique des deux paradigmes :

| Dimension d'analyse | **Nudges (Thaler & Sunstein)** | **Boosts (Hertwig & Grüne-Yanoff)** |
|---|---|---|
| **Cible d'intervention** | L'architecture externe du choix et l'environnement décisionnel. | Les compétences cognitives, procédurales et heuristiques de l'agent. |
| **Mécanisme cognitif** | Exploitation des biais (inertie, ancrage, cadrage) sans nécessiter d'effort réflexif. | Autonomisation de l'usager par l'apprentissage de règles décisionnelles simples (*fast-and-frugal heuristics*). |
| **Effort requis de l'usager** | Nul ou passif (l'individu suit le chemin de moindre résistance). | Actif (l'usager doit investir un effort d'apprentissage initial). |
| **Pérennité dans le temps** | **Effet transitoire :** Le comportement dévie ou s'estompe fréquemment dès que le nudge est retiré (*decay effect*). | **Effet pérenne :** La compétence acquise demeure intégrée et continue d'opérer durablement. |
| **Transférabilité** | Nulle (l'effet est strictement circonscrit au contexte physique agencé). | Élevée (l'individu peut transposer la compétence heuristique à d'autres domaines d'action). |
| **Exemple représentatif** | Option par défaut sur un régime d'épargne ou assiette plus petite. | Représentation en fréquences naturelles pour évaluer un risque médical ou arbre de décision simple. |

---

### [Page 204]

### 9. L'EFFICACITÉ EMPIRIQUE DU NUDGE SUR LE TERRAIN

#### 9.1. Les interventions dans le domaine du don d'organes
Le cas du don d'organes illustre la puissance comportementale spectaculaire des règles par défaut (*defaults*). Dans les régimes de consentement explicite (*opt-in*, où le citoyen doit poser une action active pour s'inscrire au registre des donneurs), les taux de consentement plafonnent souvent sous la barre des 15 à 20 % (comme en Allemagne). À l'inverse, dans les régimes de consentement présumé (*opt-out*, où chaque citoyen est présumé donneur à moins de manifester son refus), les taux d'adhésion administrative dépassent régulièrement 95 % (comme en Autriche ou en France).

Toutefois, Congiu et Moscati rappellent un point clinique fondamental souvent éludé : **l'efficacité administrative ne se traduit pas automatiquement en prélèvements d'organes effectifs**. Dans la pratique hospitalière réelle, les équipes médicales consultent presque systématiquement les familles endeuillées avant tout prélèvement. Si l'acceptabilité sociale et la communication avec les proches n'ont pas été préparées de manière éthique, le taux de refus des familles neutralise le bénéfice de l'option par défaut.

---

### [Page 205]

#### 9.2. Les normes sociales et l'énergie : l'expérience O-Power
L'une des interventions les plus célèbres et les plus documentées sur les normes sociales est le programme d'efficacité énergétique mené par la société O-Power auprès de millions de ménages américains (Allcott, 2011).

Le dispositif repose sur l'envoi de rapports périodiques de consommation électrique combinant deux niveaux normatifs :
1. **La norme descriptive :** Comparer la consommation d'électricité du foyer à celle de ménages comparables du même voisinage. Les ménages surconsommateurs réduisent leur consommation de 2 à 3 % en constatant l'écart.
2. **La norme injonctive (la neutralisation de l'effet boomerang) :** Sans précaution particulière, les ménages les plus économes, en apprenant qu'ils consomment nettement moins que la moyenne, auraient tendance à relâcher leur vigilance et à consommer davantage pour se caler sur la norme : c'est le redoutable **effet boomerang**. Pour neutraliser ce phénomène, O-Power a adjoint une norme injonctive signifiant l'approbation sociale explicite de la sobriété énergétique sous la forme d'un symbole valorisant (un émoticône souriant « smiley » ou la mention « Excellent »). Cette approbation sociale fige la conduite sobre et prévient tout relâchement.

---

### [Page 206]

#### 9.3. La conformité fiscale au Royaume-Uni
Dans le domaine des rentrées fiscales, l'équipe comportementale britannique (*Behavioural Insights Team* / Nudge Unit) a expérimenté l'adjonction d'une simple phrase dans les lettres de relance envoyées aux contribuables en retard de paiement : 
> *« 9 personnes sur 10 dans votre région paient leurs impôts à temps. »*

Cette formulation rend visible la norme descriptive collective. En constatant que le comportement civique est la norme partagée par la quasi-totalité de leurs pairs, les retardataires accélèrent le paiement de leurs dettes fiscales sans qu'aucune augmentation de pénalité financière n'ait été requise (Hallsworth et al., 2017).

---

### [Page 207]

#### 9.4. Efficacité à long terme et risques d'éviction (*Crowding-Out*)
La littérature récente met en garde contre deux dérives d'appréciation :
1. **L'estompage temporel :** Si les nudges produisent des effets immédiats saisissants, de nombreuses études longitudinales documentent une érosion progressive de l'efficacité lorsque l'effet de nouveauté disparaît ou que les usagers développent une habitude de résistance.
2. **Le risque de substitution politique (*Crowding-Out*) :** L'illusion qu'un problème sociétal complexe (le réchauffement climatique, les inégalités de santé, le sous-financement des retraites) pourrait être résolu à moindre coût par quelques « coups de pouce » psychologiques peut détourner les gouvernements de mesures structurelles indispensables, telles que la taxe carbone, les investissements d'infrastructures ou les réformes fiscales d'envergure.

---

### [Page 208]

### 10. CONCLUSION ET PERSPECTIVES DE RECHERCHE

Au terme de cet état des lieux critique, Congiu et Moscati dressent un bilan balancé du mouvement des nudges. L'économie comportementale appliquée a indéniablement enrichi la boîte à outils de l'action publique en substituant au modèle désincarné de l'Homo Economicus une vision réaliste et empirique de la psychologie humaine.

Toutefois, la notion de nudge souffre encore d'un flou taxinomique certain, englobant sous un même vocable des interventions aussi disparates que des incitations visuelles automatiques (Type 1) et des programmes d'information réflexive (Type 2). 

Sur le plan éthique et clinique, la préservation de l'autonomie citoyenne demeure la pierre de touche : les décideurs doivent privilégier la transparence des interventions, renoncer aux pratiques manipulatrices des architectures de choix opaques et articuler harmonieusement les nudges d'environnement immédiat avec des stratégies de renforcement des compétences durables (*boosts*).

---

### NOTES & RÉFÉRENCES MAJEURES

* **Allcott, H. (2011).** Social norms and energy conservation. *Journal of Public Economics*, 95(9–10), 1082–1095.
* **Bovens, L. (2009).** The ethics of nudge. In *Preference change* (pp. 207–219). Springer.
* **Hansen, P. G. (2016).** The definition of nudge and libertarian paternalism: Does the hand fit the glove? *European Journal of Risk Regulation*, 7(1), 155–174.
* **Hansen, P. G., & Jespersen, A. M. (2013).** Nudge and the manipulation of choice: A framework for the responsible use of the nudge approach to behaviour change in public policy. *European Journal of Risk Regulation*, 4(1), 3–28.
* **Hausman, D. M., & Welch, B. (2010).** Debate: To nudge or not to nudge. *Journal of Political Philosophy*, 18(1), 123–136.
* **Hertwig, R., & Grüne-Yanoff, T. (2017).** Nudging and boosting: Steering or empowering good decisions. *Perspectives on Psychological Science*, 12(6), 973–986.
* **Homonoff, T. A. (2018).** Can small incentives have large effects? The impact of taxes versus bonuses on disposable bag use. *American Economic Journal: Economic Policy*, 10(4), 177–210.
* **Huber, J., Payne, J. W., & Puto, C. (1982).** Adding asymmetrically dominated alternatives: Violations of regularity and the similarity hypothesis. *Journal of Consumer Research*, 9(1), 90–98.
* **Schultz, P. W., Nolan, J. M., Cialdini, R. B., Goldstein, N. J., & Griskevicius, V. (2007).** The constructive, destructive, and reconstructive power of social norms. *Psychological Science*, 18(5), 429–434.
* **Sunstein, C. R. (2014).** *Why nudge? The politics of libertarian paternalism*. Yale University Press.
* **Sunstein, C. R. (2017).** Nudges that fail. *Behavioural Public Policy*, 1(1), 4–25.
* **Thaler, R. H., & Sunstein, C. R. (2008).** *Nudge: Improving decisions about health, wealth, and happiness*. Yale University Press.
"""
