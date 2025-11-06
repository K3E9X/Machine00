# ⚡ Solution Rapide - App qui dort

## 🔍 Problème

Votre app affiche :
```
Zzzz
This app has gone to sleep due to inactivity.
Would you like to wake it back up?
```

**Cause :** Plan gratuit Streamlit Cloud met en veille après 7 jours d'inactivité.

---

## ✅ Solution Immédiate (5 minutes) - RECOMMANDÉE

### Option 1 : UptimeRobot (Gratuit, Simple)

**C'est la meilleure solution pour vous !**

1. **Allez sur** https://uptimerobot.com/

2. **Créez un compte gratuit** (email + mot de passe)

3. **Cliquez sur "Add New Monitor"**

4. **Remplissez :**
   ```
   Monitor Type: HTTP(s)
   Friendly Name: Security Audit App
   URL: https://app-security-audit.streamlit.app/
   Monitoring Interval: Every 5 minutes
   ```

5. **Cliquez "Create Monitor"**

✅ **C'est tout ! Votre app ne dormira plus.**

**Vérification :**
- Vous recevrez un email de confirmation
- Le dashboard UptimeRobot affichera votre monitor
- Statut : UP (vert) = tout est OK

---

### Option 2 : GitHub Action (Déjà configuré)

**J'ai créé un workflow automatique pour vous !**

**Fichier créé :** `.github/workflows/keep-app-alive.yml`

**Ce que ça fait :**
- Ping votre app tous les jours à 8h UTC
- Ping supplémentaire tous les 3 jours à 14h UTC
- Empêche la mise en veille

**Activation :**
1. Commitez et pushez le fichier `.github/workflows/keep-app-alive.yml`
2. Allez sur GitHub → Onglet "Actions"
3. Vous verrez "Keep Streamlit App Alive"
4. Le workflow s'exécute automatiquement selon le planning

**Test manuel :**
1. GitHub → Actions
2. "Keep Streamlit App Alive"
3. "Run workflow" → "Run workflow"
4. Vérifiez les logs

---

## 🎯 Quelle Solution Choisir ?

### Recommandation : **Option 1 (UptimeRobot)**

**Pourquoi ?**
- ✅ Plus simple (5 minutes)
- ✅ Ping toutes les 5 minutes (vs 1x/jour GitHub)
- ✅ Dashboard de monitoring inclus
- ✅ Emails d'alerte si app down
- ✅ Pas besoin de toucher au code

**Option 2 utile si :**
- Vous voulez tout dans GitHub
- Vous ne voulez pas compte externe
- 1 ping/jour suffit (app peu utilisée)

---

## 💡 Pourquoi ça arrive ?

**Streamlit Cloud Gratuit :**
- Ressources partagées
- Mise en veille si pas d'activité pendant 7 jours
- Normal et attendu sur plan gratuit

**Ce n'est PAS un bug !**

---

## 🚀 Si vous voulez éliminer complètement le problème

### Option A : Streamlit Cloud Pro (~€200/mois)

**Bénéfices :**
- Pas de mise en veille (always-on)
- Plus de ressources (4GB RAM)
- Support prioritaire
- Apps privées avec authentification

**Quand upgrader :**
- Application en production
- Clients payants
- Plus de 100 utilisateurs/jour

### Option B : VPS Auto-hébergé (~€5-10/mois)

**Fournisseurs :**
- DigitalOcean : $6/mois
- Hetzner : €4/mois
- OVH : €5/mois

**Avantages :**
- Contrôle total
- Pas de limitations
- Moins cher long terme

**Inconvénient :**
- Configuration serveur nécessaire
- Maintenance à faire

---

## ❓ FAQ Rapide

**Q : L'app va-t-elle perdre mes données ?**
R : Non, la mise en veille n'affecte que la disponibilité, pas les données.

**Q : Combien de temps pour réveiller l'app ?**
R : 20-30 secondes en moyenne.

**Q : UptimeRobot est-il vraiment gratuit ?**
R : Oui, plan gratuit inclut 50 monitors avec check toutes les 5 minutes.

**Q : Et si j'ai beaucoup d'utilisateurs ?**
R : UptimeRobot ou GitHub Action suffisent jusqu'à ~100 utilisateurs/jour. Au-delà, considérez Streamlit Pro.

**Q : Est-ce que Streamlit va bannir mon app si j'utilise UptimeRobot ?**
R : Non, c'est une pratique courante et acceptée.

---

## 🎬 Action Maintenant

**Faites ça maintenant (5 minutes) :**

1. ✅ Ouvrez https://uptimerobot.com/
2. ✅ Créez un compte
3. ✅ Ajoutez le monitor (voir Option 1 ci-dessus)
4. ✅ Vérifiez que le statut est "UP"

**Et c'est réglé pour toujours !** 🎉

---

## 📞 Support

Si vous avez des problèmes :

1. **App ne se réveille pas :**
   - Dashboard Streamlit → "Manage app" → "Reboot app"

2. **UptimeRobot ne fonctionne pas :**
   - Vérifiez l'URL : `https://app-security-audit.streamlit.app/`
   - Vérifiez l'intervalle : 5 minutes
   - Attendez 10 minutes pour le premier check

3. **GitHub Action ne s'exécute pas :**
   - Vérifiez que le fichier est sur `main`
   - Allez dans Actions → vérifiez les permissions
   - Lancez manuellement pour tester

---

**Créé le :** 2025-10-30
**Votre app :** https://app-security-audit.streamlit.app/

**Document détaillé :** Voir `TROUBLESHOOTING_SLEEP.md` pour toutes les options
