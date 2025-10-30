translations = {
    "fr": {
        "app_title": "Évaluation de Sécurité Applicative",
        "app_subtitle": "Questionnaire basé sur OWASP Top 10, ISO 27001 et ANSSI",

        # Navigation
        "nav_home": "Accueil",
        "nav_questionnaire": "Questionnaire",
        "nav_results": "Résultats",

        # Home page
        "home_welcome": "Bienvenue",
        "home_description": "Cet outil vous permet d'évaluer rapidement le niveau de sécurité de vos applications web et d'identifier celles nécessitant un audit approfondi.",
        "home_features_title": "Fonctionnalités",
        "home_feature1": "Questionnaire structuré basé sur les standards internationaux",
        "home_feature2": "Scoring automatique et analyse par catégorie",
        "home_feature3": "Recommandations personnalisées",
        "home_feature4": "Export Excel pour partage avec les clients",
        "home_feature5": "Support multilingue (Français/Anglais)",
        "home_feature6": "Interface moderne et intuitive",
        "home_start": "Démarrer une évaluation",
        "home_template": "Télécharger le modèle Excel",

        # Questionnaire
        "quest_title": "Questionnaire de Sécurité",
        "quest_app_info": "Informations Application",
        "quest_app_name": "Nom de l'application",
        "quest_app_name_placeholder": "Ex: Application CRM",
        "quest_owner": "Propriétaire",
        "quest_owner_placeholder": "Ex: Direction Métier",
        "quest_contact": "Contact",
        "quest_contact_placeholder": "Ex: john.doe@company.com",
        "quest_environment": "Environnement",
        "quest_description": "Description",
        "quest_description_placeholder": "Brève description de l'application",
        "quest_progress": "Progression",
        "quest_category": "Catégorie",
        "quest_question": "Question",
        "quest_select": "Sélectionnez une réponse",
        "quest_submit": "Soumettre l'évaluation",
        "quest_required": "Veuillez répondre à toutes les questions avant de soumettre",
        "quest_standards": "Standards",

        # Results
        "results_title": "Résultats de l'Évaluation",
        "results_overall_score": "Score Global",
        "results_risk_level": "Niveau de Risque",
        "results_recommendation": "Recommandation",
        "results_category_breakdown": "Détail par Catégorie",
        "results_recommendations": "Recommandations d'Amélioration",
        "results_no_recommendations": "Excellent travail ! Aucune recommandation critique.",
        "results_severity": "Sévérité",
        "results_high": "Élevée",
        "results_medium": "Moyenne",
        "results_export": "Exporter en Excel",
        "results_new_assessment": "Nouvelle évaluation",

        # Common
        "loading": "Chargement...",
        "error": "Erreur",
        "success": "Succès",
        "back": "Retour",
        "next": "Suivant",
        "previous": "Précédent",
    },
    "en": {
        "app_title": "Application Security Assessment",
        "app_subtitle": "Questionnaire based on OWASP Top 10, ISO 27001 and ANSSI",

        # Navigation
        "nav_home": "Home",
        "nav_questionnaire": "Questionnaire",
        "nav_results": "Results",

        # Home page
        "home_welcome": "Welcome",
        "home_description": "This tool allows you to quickly assess the security level of your web applications and identify those requiring a thorough audit.",
        "home_features_title": "Features",
        "home_feature1": "Structured questionnaire based on international standards",
        "home_feature2": "Automatic scoring and category-wise analysis",
        "home_feature3": "Personalized recommendations",
        "home_feature4": "Excel export for client sharing",
        "home_feature5": "Multi-language support (French/English)",
        "home_feature6": "Modern and intuitive interface",
        "home_start": "Start Assessment",
        "home_template": "Download Excel Template",

        # Questionnaire
        "quest_title": "Security Questionnaire",
        "quest_app_info": "Application Information",
        "quest_app_name": "Application Name",
        "quest_app_name_placeholder": "Ex: CRM Application",
        "quest_owner": "Owner",
        "quest_owner_placeholder": "Ex: Business Unit",
        "quest_contact": "Contact",
        "quest_contact_placeholder": "Ex: john.doe@company.com",
        "quest_environment": "Environment",
        "quest_description": "Description",
        "quest_description_placeholder": "Brief application description",
        "quest_progress": "Progress",
        "quest_category": "Category",
        "quest_question": "Question",
        "quest_select": "Select an answer",
        "quest_submit": "Submit Assessment",
        "quest_required": "Please answer all questions before submitting",
        "quest_standards": "Standards",

        # Results
        "results_title": "Assessment Results",
        "results_overall_score": "Overall Score",
        "results_risk_level": "Risk Level",
        "results_recommendation": "Recommendation",
        "results_category_breakdown": "Category Breakdown",
        "results_recommendations": "Improvement Recommendations",
        "results_no_recommendations": "Excellent work! No critical recommendations.",
        "results_severity": "Severity",
        "results_high": "High",
        "results_medium": "Medium",
        "results_export": "Export to Excel",
        "results_new_assessment": "New Assessment",

        # Common
        "loading": "Loading...",
        "error": "Error",
        "success": "Success",
        "back": "Back",
        "next": "Next",
        "previous": "Previous",
    }
}

def get_text(key: str, lang: str = "fr") -> str:
    """Get translated text for a given key"""
    return translations.get(lang, translations["fr"]).get(key, key)
