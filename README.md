# Security Assessment Tool - Audit de Sécurité AppSec

Outil professionnel de questionnaire de sécurité pour l'audit des applications web et infrastructure. Basé sur les standards OWASP Top 10, ISO 27001 et les recommandations de l'ANSSI.

## Vue d'ensemble

Cet outil permet d'évaluer rapidement le niveau de sécurité d'applications et d'identifier celles nécessitant un audit complet. Conçu pour gérer l'audit de centaines d'applications simultanément (jusqu'à 800+).

### Fonctionnalités principales

- **Questionnaire structuré** : 40+ questions organisées en 7 catégories basées sur les standards internationaux
- **Scoring automatique** : Calcul du score de sécurité et identification du niveau de risque
- **Recommandations personnalisées** : Suggestions d'amélioration basées sur les faiblesses identifiées
- **Export Excel** : Génération de rapports détaillés et templates de questionnaire
- **Multilingue** : Support complet français/anglais
- **Interface moderne** : Design minimaliste et professionnel inspiré des plateformes GAFAM
- **API REST** : Architecture découplée pour intégration facile

## Architecture

### Stack technique

**Backend**
- Python 3.x
- Flask (API REST)
- openpyxl (Export Excel)

**Frontend**
- React 18
- i18next (Internationalisation)
- Axios (Client HTTP)

### Structure du projet

```
Machine00/
├── backend/
│   ├── app.py                  # Application Flask principale
│   ├── requirements.txt        # Dépendances Python
│   ├── models/
│   │   └── questionnaire.py    # Modèle de données et scoring
│   ├── services/
│   │   └── excel_export.py     # Service d'export Excel
│   ├── routes/
│   │   └── api.py              # Routes API
│   └── data/
│       └── questions.json      # Base de questions
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── index.js
│       ├── App.js
│       ├── pages/
│       │   ├── Home.js
│       │   ├── Questionnaire.js
│       │   └── Results.js
│       ├── locales/
│       │   ├── fr.json
│       │   └── en.json
│       ├── utils/
│       │   ├── api.js
│       │   └── i18n.js
│       └── styles/
│           └── App.css
└── README.md
```

## Installation

### Prérequis

- Python 3.8+
- Node.js 16+
- npm ou yarn

### Backend

```bash
cd backend
pip install -r requirements.txt
```

### Frontend

```bash
cd frontend
npm install
```

## Démarrage

### Backend

```bash
cd backend
python app.py
```

Le serveur démarre sur `http://localhost:5000`

### Frontend

```bash
cd frontend
npm start
```

L'application web démarre sur `http://localhost:3000`

## Utilisation

### 1. Évaluation via l'interface web

1. Accédez à `http://localhost:3000`
2. Cliquez sur "Démarrer une évaluation"
3. Remplissez les informations de l'application
4. Répondez aux questions par catégorie
5. Soumettez le questionnaire pour obtenir les résultats
6. Exportez le rapport en Excel si nécessaire

### 2. Export de template Excel

L'outil permet de générer des templates Excel vierges pour distribution :

- Via l'interface : Bouton "Télécharger le modèle Excel" sur la page d'accueil
- Via l'API : `GET /api/export/template?lang=fr&app_name=MonApp`

Les clients peuvent remplir le template Excel et le retourner pour analyse.

### 3. Utilisation de l'API

#### Récupérer les questions

```bash
GET /api/questions?lang=fr
```

#### Soumettre un questionnaire

```bash
POST /api/submit
Content-Type: application/json

{
  "responses": {
    "iam_001": 10,
    "iam_002": 7,
    ...
  },
  "app_info": {
    "name": "Application CRM",
    "owner": "Direction Marketing",
    "contact": "contact@example.com",
    "environment": "Production",
    "description": "Application de gestion clients"
  },
  "lang": "fr"
}
```

#### Exporter les résultats en Excel

```bash
POST /api/export/results
Content-Type: application/json

{
  "responses": {...},
  "app_info": {...},
  "lang": "fr"
}
```

## Catégories d'évaluation

### 1. Gestion des Identités et des Accès (IAM)
- Authentification multi-facteurs
- Politique de mots de passe
- Gestion des sessions
- Contrôle d'accès (RBAC/ABAC)
- Séparation des comptes privilégiés
- Single Sign-On (SSO)

### 2. Architecture Réseau et Segmentation
- Segmentation réseau (DMZ, zones de confiance)
- Pare-feu multi-zones
- Web Application Firewall (WAF)
- Documentation des flux
- Chiffrement TLS/SSL
- IDS/IPS

### 3. Flux et Interconnexions
- Sécurité des API
- Connexions vers systèmes tiers
- Chiffrement des échanges
- Passerelle/Proxy
- Tests de sécurité des interconnexions

### 4. Hébergement et Infrastructure
- Type d'hébergement
- Redondance et haute disponibilité
- Sauvegardes et PRA/PCA
- Gestion des patches
- Supervision et alertes
- Conteneurs et orchestration

### 5. Sécurité des Données
- Chiffrement au repos
- Classification des données
- Prévention de fuite (DLP)
- Conformité RGPD
- Rétention et purge
- Audit des bases de données

### 6. Sécurité Applicative
- Tests OWASP Top 10
- Processus de développement sécurisé (SSDLC)
- Analyse des dépendances (SCA)
- Validation des entrées
- Tests dans CI/CD
- Pentests externes

### 7. Journalisation et Surveillance
- Journalisation des événements de sécurité
- Protection des logs
- Corrélation et analyse (SIEM)
- Politique de rétention

## Système de scoring

### Calcul du score

- Chaque question a un poids spécifique
- Chaque réponse a une valeur (0-10 ou 0-15 points)
- Score total = Σ (valeur_réponse × poids_question)
- Pourcentage = (score_obtenu / score_maximum) × 100

### Niveaux de risque

| Score | Niveau | Couleur |
|-------|--------|---------|
| 80-100% | Risque Faible | Vert |
| 60-79% | Risque Modéré | Orange |
| 40-59% | Risque Élevé | Rouge |
| 0-39% | Risque Critique | Rouge foncé |

### Recommandations d'audit

| Score | Catégories critiques | Recommandation |
|-------|---------------------|----------------|
| <50% | ≥3 catégories <50% | Audit Complet Requis |
| 50-69% | ≥1 catégorie <50% | Audit Ciblé Recommandé |
| ≥70% | Toutes >50% | Revue Légère Suffisante |

## Cas d'usage : Audit de 800 applications

### Workflow recommandé

1. **Phase de distribution**
   - Générer des templates Excel personnalisés pour chaque application
   - Distribuer aux équipes responsables
   - Définir une deadline de retour

2. **Phase de collecte**
   - Récupération des templates complétés
   - Import des réponses via l'API ou interface web
   - Génération automatique des scores

3. **Phase d'analyse**
   - Tri des applications par niveau de risque
   - Identification des applications critiques (score <50%)
   - Priorisation des audits complets

4. **Phase de reporting**
   - Export des rapports Excel détaillés
   - Présentation des résultats aux stakeholders
   - Planification des audits de sécurité

### Automatisation via API

Pour traiter 800 applications, utilisez l'API :

```python
import requests
import json

API_URL = "http://localhost:5000/api"

# Charger les réponses depuis vos fichiers Excel
applications = load_applications_from_excel()

results = []
for app in applications:
    response = requests.post(f"{API_URL}/submit", json={
        "responses": app["responses"],
        "app_info": app["info"],
        "lang": "fr"
    })
    results.append(response.json())

# Trier par score
critical_apps = [r for r in results if r["score"]["percentage"] < 50]
high_risk_apps = [r for r in results if 50 <= r["score"]["percentage"] < 70]

print(f"Applications critiques nécessitant un audit complet: {len(critical_apps)}")
print(f"Applications à risque élevé nécessitant un audit ciblé: {len(high_risk_apps)}")
```

## Standards et références

- **OWASP Top 10** : https://owasp.org/www-project-top-ten/
- **ISO/IEC 27001** : Standard international de gestion de la sécurité de l'information
- **ANSSI** : Agence Nationale de la Sécurité des Systèmes d'Information (France)
- **RGPD** : Règlement Général sur la Protection des Données

## Personnalisation

### Ajouter des questions

Modifiez le fichier `backend/data/questions.json` :

```json
{
  "id": "custom_001",
  "text": {
    "fr": "Votre question en français",
    "en": "Your question in English"
  },
  "category": "category_id",
  "weight": 5,
  "standard": ["OWASP A01", "Custom Standard"],
  "options": [
    {"value": 0, "label": {"fr": "Non", "en": "No"}},
    {"value": 10, "label": {"fr": "Oui", "en": "Yes"}}
  ]
}
```

### Modifier les seuils de risque

Éditez `backend/models/questionnaire.py`, méthode `_determine_risk_level()`.

### Ajouter une langue

1. Créez `frontend/src/locales/[code].json`
2. Ajoutez la langue dans `frontend/src/utils/i18n.js`
3. Ajoutez les traductions dans `backend/data/questions.json`

## Secteurs d'application

L'outil est adapté à tous les secteurs :

- **Luxe** : Protection des données clients et marque
- **Retail** : Sécurité e-commerce et paiements
- **Services numériques** : Conformité et disponibilité
- **Finance** : Conformité réglementaire stricte
- **Santé** : Protection données personnelles de santé
- **Industrie** : Sécurité OT/IT

## Développement

### Tests

Backend :
```bash
cd backend
python -m pytest
```

Frontend :
```bash
cd frontend
npm test
```

### Build de production

Frontend :
```bash
cd frontend
npm run build
```

Les fichiers statiques sont générés dans `frontend/build/`

## Contribution

Pour contribuer au projet :

1. Fork le repository
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## License

Ce projet est un outil interne d'audit de sécurité.

## Support

Pour toute question ou problème :
- Consultez la documentation
- Ouvrez une issue sur le repository
- Contactez l'équipe de sécurité

## Roadmap

- [ ] Support de langues supplémentaires (ES, DE, IT)
- [ ] Dashboard d'analyse multi-applications
- [ ] Intégration avec outils SIEM
- [ ] Module de suivi des remédiations
- [ ] API GraphQL
- [ ] Application mobile
