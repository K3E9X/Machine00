# Security Assessment Tool - Version Streamlit

Outil professionnel de questionnaire de sécurité pour l'audit des applications web et infrastructure. Basé sur les standards OWASP Top 10, ISO 27001 et les recommandations de l'ANSSI.

**Version Streamlit optimisée pour le déploiement cloud facile**

## 🚀 Application en Ligne

**🔗 DEMO EN DIRECT :** https://app-security-audit.streamlit.app/

Essayez l'application immédiatement, aucune installation requise !

## Démarrage rapide

### Installation locale

```bash
pip install -r requirements.txt
```

### Lancement

```bash
streamlit run app.py
```

L'application s'ouvre automatiquement sur `http://localhost:8501`

## Déploiement sur Streamlit Cloud

### En 3 étapes simples :

1. **Push sur GitHub** (déjà fait si vous clonez ce repo)
2. **Créez un compte sur** https://share.streamlit.io/
3. **Déployez** : Sélectionnez ce repository et `app.py`

**→ Votre app est en ligne en 2 minutes !**

Guide détaillé : [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md)

## Fonctionnalités

- **Questionnaire interactif** : 40+ questions sur 7 catégories de sécurité
- **Scoring automatique** : Évaluation instantanée avec niveau de risque
- **Recommandations personnalisées** : Suggestions basées sur les points faibles
- **Export Excel** : Rapports détaillés et templates
- **Multilingue** : Français/Anglais (changement à la volée)
- **Interface moderne** : Design professionnel inspiré GAFAM
- **Déploiement facile** : Streamlit Cloud gratuit

## Architecture

```
Machine00/
├── app.py                          # Application Streamlit principale
├── requirements.txt                # Dépendances Python
├── streamlit_app/
│   ├── data/
│   │   └── questions.json         # Base de questions (FR/EN)
│   └── utils/
│       ├── questionnaire.py       # Logique de scoring
│       ├── excel_export.py        # Génération Excel
│       └── translations.py        # Textes multilingues
└── .streamlit/
    └── config.toml                # Configuration thème
```

## Utilisation

### 1. Page d'accueil

- **Démarrer une évaluation** : Lance le questionnaire
- **Télécharger template Excel** : Pour distribution aux clients

### 2. Questionnaire

- Remplissez les informations de l'application
- Répondez aux questions par catégorie (onglets)
- La progression est affichée en temps réel
- Soumettez quand 100% complété

### 3. Résultats

- **Score global** : Pourcentage et niveau de risque
- **Analyse par catégorie** : Détail des points forts/faibles
- **Recommandations** : Actions prioritaires
- **Export Excel** : Rapport complet téléchargeable

## Catégories d'évaluation

1. **Gestion des Identités et Accès (IAM)** - 20%
   - MFA, mots de passe, sessions, RBAC/ABAC, SSO

2. **Architecture Réseau** - 18%
   - Segmentation, firewall, WAF, flux, chiffrement, IDS/IPS

3. **Flux et Interconnexions** - 15%
   - API, systèmes tiers, chiffrement, passerelle, tests

4. **Hébergement et Infrastructure** - 17%
   - Type d'hébergement, HA, sauvegardes, patches, monitoring, conteneurs

5. **Sécurité des Données** - 18%
   - Chiffrement, classification, DLP, RGPD, rétention, audit

6. **Sécurité Applicative** - 20%
   - OWASP Top 10, SSDLC, SCA, validation, CI/CD, pentests

7. **Journalisation et Surveillance** - 12%
   - Logs, protection, SIEM, rétention

## Scoring

### Calcul

- Score = Σ (réponse × poids_question)
- Pourcentage = score / score_max × 100

### Niveaux de risque

| Score | Risque | Couleur |
|-------|--------|---------|
| 80-100% | Faible | Vert |
| 60-79% | Modéré | Orange |
| 40-59% | Élevé | Rouge |
| 0-39% | Critique | Rouge foncé |

### Recommandations d'audit

| Score | Recommandation |
|-------|----------------|
| <50% ou 3+ catégories <50% | **Audit Complet Requis** |
| 50-69% ou 1+ catégorie <50% | **Audit Ciblé Recommandé** |
| ≥70% | **Revue Légère Suffisante** |

## Cas d'usage : 800 applications

### Workflow

1. **Distribution**
   - Téléchargez le template Excel
   - Envoyez-le aux 800 responsables d'applications
   - Fixez une deadline

2. **Collecte**
   - Recevez les fichiers complétés
   - Saisissez les réponses dans l'outil (ou via API si automatisé)

3. **Analyse**
   - Triez par score
   - Identifiez les critiques (<50%)
   - Priorisez les audits complets

4. **Reporting**
   - Exportez tous les rapports Excel
   - Présentez aux stakeholders
   - Planifiez les audits

### Optimisation pour volume

Pour traiter 800 apps efficacement :

**Option 1 : Interface web**
- Créez un formulaire par application
- Utilisez l'URL partagée de Streamlit Cloud
- Bookmark les évaluations en cours (session state)

**Option 2 : Script Python + API locale**
```python
import streamlit as st
from streamlit_app.utils.questionnaire import QuestionnaireModel

# Charger les données
model = QuestionnaireModel()

# Traiter en batch
for app in applications:
    score = model.calculate_score(app['responses'])
    recommendations = model.get_recommendations(app['responses'], 'fr')
    # Sauvegarder résultats
```

**Option 3 : Backend API séparé**
- Utilisez le backend Flask fourni (`backend/app.py`)
- API REST pour automatisation complète
- Frontend Streamlit pour visualisation

## Standards de référence

- **OWASP Top 10** : https://owasp.org/www-project-top-ten/
- **ISO/IEC 27001** : Norme internationale ISMS
- **ANSSI** : Guides de l'Agence Nationale française
- **RGPD** : Conformité données personnelles

## Personnalisation

### Ajouter des questions

Éditez `streamlit_app/data/questions.json` :

```json
{
  "id": "custom_001",
  "text": {
    "fr": "Votre question",
    "en": "Your question"
  },
  "category": "iam",
  "weight": 5,
  "standard": ["Custom Standard"],
  "options": [
    {"value": 0, "label": {"fr": "Non", "en": "No"}},
    {"value": 10, "label": {"fr": "Oui", "en": "Yes"}}
  ]
}
```

### Modifier le thème

Éditez `.streamlit/config.toml` :

```toml
[theme]
primaryColor = "#VOTRE_COULEUR"
backgroundColor = "#FFFFFF"
```

### Ajouter une langue

1. Ajoutez les traductions dans `streamlit_app/utils/translations.py`
2. Ajoutez les textes dans `streamlit_app/data/questions.json`
3. Mettez à jour le sélecteur de langue dans `app.py`

## Secteurs d'application

- **Luxe** : Protection marque et données clients VIP
- **Retail** : Sécurité e-commerce et moyens de paiement
- **Services numériques** : Conformité et disponibilité
- **Finance** : Réglementations strictes (PCI-DSS, etc.)
- **Santé** : Données personnelles de santé
- **Industrie** : Sécurité OT/IT convergence

## Avantages de la version Streamlit

✅ **Déploiement ultra-rapide** : 2 minutes sur Streamlit Cloud
✅ **Gratuit** : Plan gratuit suffisant pour démarrer
✅ **Pas de frontend à gérer** : Tout en Python
✅ **Interface moderne** : Design professionnel automatique
✅ **Responsive** : Fonctionne sur mobile/tablette
✅ **HTTPS inclus** : Sécurité native
✅ **Updates automatiques** : Push Git = déploiement auto

## Comparaison versions

| Fonctionnalité | Streamlit | React + Flask |
|----------------|-----------|---------------|
| Déploiement | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Maintenance | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Customisation UI | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Performance | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Évolutivité | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Coût | Gratuit | Payant (hosting) |

**Recommandation** : Streamlit pour démarrage rapide et POC, React+Flask pour production à large échelle.

## Limitations

### Streamlit Cloud gratuit

- 1 GB RAM (suffisant pour usage normal)
- Pas de persistance de données (utilisez export Excel)
- Mise en veille après inactivité
- 1 app publique gratuite

### Solutions

- **Plus de ressources** : Streamlit Cloud Pro (~$200/mois)
- **Multiple apps** : Google Cloud Run, AWS ECS
- **Données persistantes** : Ajoutez une base de données externe
- **Haute disponibilité** : Déployez sur infrastructure cloud

## Support et documentation

- **Guide de déploiement** : [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md)
- **Documentation Streamlit** : https://docs.streamlit.io/
- **OWASP** : https://owasp.org/
- **ISO 27001** : https://www.iso.org/isoiec-27001-information-security.html

## Développement

### Structure du code

```python
# app.py - Point d'entrée
def main():
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'questionnaire':
        render_questionnaire()
    elif st.session_state.page == 'results':
        render_results()
```

### État de session

Streamlit utilise `st.session_state` pour la navigation et les données :

```python
st.session_state.page = 'home' | 'questionnaire' | 'results'
st.session_state.lang = 'fr' | 'en'
st.session_state.responses = {question_id: value}
st.session_state.app_info = {...}
st.session_state.results = {...}
```

### Ajout de fonctionnalités

Pour ajouter une nouvelle page :

1. Créez la fonction `render_new_page()`
2. Ajoutez la condition dans `main()`
3. Ajoutez le bouton de navigation

## Roadmap

- [ ] Dashboard multi-applications
- [ ] Import Excel automatique
- [ ] Export PDF
- [ ] Graphiques avancés (Plotly)
- [ ] Authentification utilisateurs
- [ ] Base de données (historique)
- [ ] API REST intégrée
- [ ] Notifications par email

## License

Outil interne d'audit de sécurité - Usage professionnel

## Auteur

Développé avec Claude Code pour l'audit de sécurité AppSec

---

**Prêt à déployer en 2 minutes sur Streamlit Cloud !** 🚀
