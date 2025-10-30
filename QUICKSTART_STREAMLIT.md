# Démarrage Ultra-Rapide - Streamlit

## Option 1 : Test en local (2 minutes)

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Lancer l'application
streamlit run app.py
```

✅ L'application s'ouvre automatiquement sur http://localhost:8501

## Option 2 : Déploiement cloud (5 minutes)

### Étape 1 : Compte Streamlit Cloud
1. Allez sur https://share.streamlit.io/
2. Cliquez sur "Continue with GitHub"
3. Autorisez Streamlit

### Étape 2 : Déploiement
1. Cliquez sur "New app"
2. Repository : `K3E9X/Machine00`
3. Branch : `claude/audit-security-appsec-011CUd39zNd2zQsouuCMRkqp`
4. Main file : `app.py`
5. Cliquez "Deploy!"

### Étape 3 : Attendez 2-3 minutes

Votre app sera accessible via une URL du type :
```
https://k3e9x-machine00-app-xxxxx.streamlit.app
```

🎉 **C'est en ligne !**

## Première utilisation

1. **Page d'accueil**
   - Changez la langue avec le bouton 🌐 FR/EN
   - Cliquez sur "▶️ Démarrer une évaluation"

2. **Questionnaire**
   - Remplissez les infos de l'application
   - Répondez aux questions (onglets par catégorie)
   - Soumettez quand 100% complété

3. **Résultats**
   - Consultez votre score et niveau de risque
   - Lisez les recommandations
   - Téléchargez le rapport Excel

## Distribution aux clients

### Pour 800 applications

**Méthode recommandée :**

1. Téléchargez le template Excel depuis la page d'accueil
2. Envoyez-le aux 800 responsables d'applications
3. Récupérez les fichiers complétés
4. Saisissez les réponses dans l'outil (ou automatisez)
5. Générez les 800 rapports
6. Priorisez les audits selon les scores

**Alternative : URL partagée**
- Partagez l'URL Streamlit Cloud
- Chaque responsable remplit le questionnaire
- Exportez individuellement les résultats

## Commandes utiles

```bash
# Test local
streamlit run app.py

# Test avec port spécifique
streamlit run app.py --server.port 8502

# Mode développement avec auto-reload
streamlit run app.py --server.runOnSave true
```

## Troubleshooting rapide

**Erreur "Module not found"**
```bash
pip install -r requirements.txt
```

**Port déjà utilisé**
```bash
streamlit run app.py --server.port 8502
```

**L'app est lente**
- Normal au premier lancement
- Streamlit compile le code

**Données perdues**
- Streamlit Cloud gratuit ne persiste pas les données
- Utilisez toujours l'export Excel

## Personnalisation rapide

**Changer les couleurs :**

Éditez `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#VOTRE_COULEUR"
```

**Ajouter des questions :**

Éditez `streamlit_app/data/questions.json`

## Support

- README complet : [README_STREAMLIT.md](README_STREAMLIT.md)
- Guide déploiement : [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md)
- Docs Streamlit : https://docs.streamlit.io/

---

**Temps total : 5 minutes de zéro à production !** ⚡
