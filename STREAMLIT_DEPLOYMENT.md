# Déploiement sur Streamlit Cloud

## Guide de déploiement rapide

### Prérequis

- Un compte GitHub (gratuit)
- Un compte Streamlit Cloud (gratuit) : https://share.streamlit.io/

### Étapes de déploiement

#### 1. Préparation du repository GitHub

Assurez-vous que votre repository GitHub contient :
- `app.py` (fichier principal de l'application)
- `requirements.txt` (dépendances Python)
- `streamlit_app/` (dossier avec les utilitaires)
- `.streamlit/config.toml` (configuration Streamlit)

#### 2. Connexion à Streamlit Cloud

1. Allez sur https://share.streamlit.io/
2. Cliquez sur "Sign up" et connectez-vous avec votre compte GitHub
3. Autorisez Streamlit à accéder à vos repositories

#### 3. Déploiement de l'application

1. Cliquez sur "New app"
2. Sélectionnez votre repository : `K3E9X/Machine00`
3. Sélectionnez la branche : `claude/audit-security-appsec-011CUd39zNd2zQsouuCMRkqp` (ou `main` après merge)
4. Fichier principal : `app.py`
5. Cliquez sur "Deploy!"

#### 4. Attendre le déploiement

Le déploiement prend généralement 2-5 minutes. Streamlit va :
- Installer les dépendances depuis `requirements.txt`
- Lancer l'application
- Vous fournir une URL publique (ex: `https://votre-app.streamlit.app`)

### URL de l'application

Une fois déployée, votre application sera accessible via une URL du type :
```
https://k3e9x-machine00-app-xxxxxxxxx.streamlit.app
```

Vous pouvez personnaliser cette URL dans les settings de Streamlit Cloud.

## Test en local avant déploiement

### Installation

```bash
pip install -r requirements.txt
```

### Lancement

```bash
streamlit run app.py
```

L'application s'ouvre automatiquement sur `http://localhost:8501`

## Configuration avancée

### Variables d'environnement

Si vous avez besoin de variables d'environnement (API keys, etc.) :

1. Dans Streamlit Cloud, allez dans "App settings"
2. Section "Secrets"
3. Ajoutez vos secrets au format TOML :

```toml
# .streamlit/secrets.toml
[secrets]
api_key = "votre_clé_api"
```

### Customisation du thème

Éditez `.streamlit/config.toml` pour personnaliser les couleurs :

```toml
[theme]
primaryColor = "#1F4E78"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F8F9FA"
textColor = "#1f2937"
```

## Limites de Streamlit Cloud (plan gratuit)

- **Ressources** : 1 GB RAM, partage de CPU
- **Stockage** : Pas de persistance de données entre redémarrages
- **Nombre d'apps** : 1 app publique gratuite
- **Uptime** : L'app se met en veille après inactivité
- **Trafic** : Pas de limite stricte pour usage raisonnable

## Upgrade vers Streamlit Cloud Pro

Pour auditer 800 applications avec :
- Plus de ressources (4 GB RAM)
- Applications privées
- Plusieurs applications
- Support prioritaire

Prix : ~$200/mois (tarif à vérifier sur streamlit.io)

## Alternatives de déploiement

### Docker + Cloud Provider

Si Streamlit Cloud ne suffit pas, déployez avec Docker :

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Déployez sur :
- **Google Cloud Run** : Simple, serverless, pay-per-use
- **AWS ECS/Fargate** : Plus de contrôle
- **Azure Container Apps** : Alternative Microsoft
- **Heroku** : Simple mais payant

### Google Cloud Run (recommandé pour 800 apps)

```bash
# Build
gcloud builds submit --tag gcr.io/PROJECT_ID/security-assessment

# Deploy
gcloud run deploy security-assessment \
  --image gcr.io/PROJECT_ID/security-assessment \
  --platform managed \
  --region europe-west1 \
  --memory 2Gi \
  --allow-unauthenticated
```

## Monitoring et maintenance

### Logs

Dans Streamlit Cloud :
1. Ouvrez votre app
2. Menu hamburger (☰) > "Manage app"
3. Onglet "Logs"

### Redéploiement

Streamlit Cloud redéploie automatiquement quand vous poussez sur la branche configurée.

Pour forcer un redéploiement :
1. "Manage app"
2. "Reboot app"

## Troubleshooting

### L'app ne démarre pas

- Vérifiez les logs dans Streamlit Cloud
- Assurez-vous que `requirements.txt` est correct
- Testez en local d'abord

### Erreur "Module not found"

- Ajoutez le module manquant dans `requirements.txt`
- Push les changements, l'app se redéploiera

### L'app est lente

- Streamlit Cloud gratuit a des ressources limitées
- Considérez :
  - Streamlit Cloud Pro
  - Déploiement sur Cloud Run avec plus de RAM
  - Optimisation du code (caching avec `@st.cache_resource`)

### Timeout lors du chargement

- L'app se met en veille après inactivité
- Premier accès après veille : ~30 secondes
- Solution : pingez l'app régulièrement ou passez à un plan payant

## Support

- Documentation Streamlit : https://docs.streamlit.io/
- Forum Streamlit : https://discuss.streamlit.io/
- GitHub issues : https://github.com/streamlit/streamlit/issues

## Checklist de déploiement

- [ ] Code testé en local
- [ ] `requirements.txt` à jour
- [ ] Repository GitHub à jour
- [ ] Compte Streamlit Cloud créé
- [ ] App déployée sur Streamlit Cloud
- [ ] URL partagée avec l'équipe
- [ ] Tests de fonctionnement complets
- [ ] Documentation mise à jour
