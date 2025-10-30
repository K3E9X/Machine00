# Démarrage Rapide - Security Assessment Tool

## Installation et lancement en 5 minutes

### Étape 1 : Installation du backend

```bash
cd backend
pip install -r requirements.txt
```

### Étape 2 : Démarrage du backend

```bash
python app.py
```

Le serveur API démarre sur http://localhost:5000

### Étape 3 : Installation du frontend (nouveau terminal)

```bash
cd frontend
npm install
```

### Étape 4 : Démarrage du frontend

```bash
npm start
```

L'application web s'ouvre automatiquement sur http://localhost:3000

## Première utilisation

1. Cliquez sur "Démarrer une évaluation"
2. Remplissez les informations de l'application (nom, propriétaire, etc.)
3. Répondez aux questions par catégorie
4. Consultez vos résultats et recommandations
5. Exportez le rapport en Excel

## Workflow pour 800 applications

### Option 1 : Distribution de templates Excel

```bash
# Via l'API
curl "http://localhost:5000/api/export/template?lang=fr" -o template.xlsx

# Distribuez ce fichier aux responsables d'applications
# Récupérez les fichiers complétés
# Importez les réponses via l'interface web
```

### Option 2 : Automatisation via API

```python
import requests

# Soumettre un questionnaire
response = requests.post('http://localhost:5000/api/submit', json={
    "responses": {
        "iam_001": 10,
        "iam_002": 7,
        # ... toutes les réponses
    },
    "app_info": {
        "name": "Mon Application",
        "owner": "Équipe IT",
        "contact": "contact@example.com"
    },
    "lang": "fr"
})

results = response.json()
print(f"Score: {results['score']['percentage']}%")
print(f"Risque: {results['score']['risk_level']['fr']}")
print(f"Recommandation: {results['score']['audit_recommendation']['fr']}")
```

## Endpoints API essentiels

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/questions` | GET | Récupérer toutes les questions |
| `/api/submit` | POST | Soumettre un questionnaire |
| `/api/export/template` | GET | Télécharger template Excel |
| `/api/export/results` | POST | Exporter résultats en Excel |
| `/api/stats` | GET | Statistiques du questionnaire |

## Changement de langue

Cliquez sur le bouton "EN/FR" en haut à droite de l'interface.

Via l'API, ajoutez `?lang=en` ou `?lang=fr` aux requêtes.

## Troubleshooting

### Le backend ne démarre pas
- Vérifiez que Python 3.8+ est installé : `python --version`
- Vérifiez que les dépendances sont installées : `pip list | grep Flask`

### Le frontend ne démarre pas
- Vérifiez que Node.js 16+ est installé : `node --version`
- Supprimez node_modules et réinstallez : `rm -rf node_modules && npm install`

### Erreur CORS
- Vérifiez que le backend tourne sur le port 5000
- Vérifiez que le frontend tourne sur le port 3000

## Support

Consultez le README.md complet pour plus d'informations.
