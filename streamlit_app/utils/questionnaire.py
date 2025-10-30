import json
from pathlib import Path
from typing import Dict, List, Optional


class QuestionnaireModel:
    def __init__(self):
        self.data_path = Path(__file__).parent.parent / "data" / "questions.json"
        self.questions_data = self._load_questions()

    def _load_questions(self) -> Dict:
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_all_questions(self, lang: str = "fr") -> Dict:
        """Return all questions in the specified language"""
        return self.questions_data

    def get_category(self, category_id: str, lang: str = "fr") -> Optional[Dict]:
        """Get a specific category by ID"""
        for category in self.questions_data["categories"]:
            if category["id"] == category_id:
                return category
        return None

    def calculate_score(self, responses: Dict[str, int]) -> Dict:
        """
        Calculate security score based on responses

        Args:
            responses: Dict mapping question_id to selected value

        Returns:
            Dict containing total score, category scores, and risk level
        """
        category_scores = {}
        total_score = 0
        total_max_score = 0

        for category in self.questions_data["categories"]:
            category_id = category["id"]
            category_score = 0
            category_max_score = 0

            for question in category["questions"]:
                question_id = question["id"]
                question_weight = question["weight"]

                # Get max possible score for this question
                max_option_value = max(opt["value"] for opt in question["options"])
                category_max_score += max_option_value * question_weight

                # Get user's response
                if question_id in responses:
                    user_value = responses[question_id]
                    category_score += user_value * question_weight

            # Calculate category percentage
            category_percentage = (category_score / category_max_score * 100) if category_max_score > 0 else 0

            category_scores[category_id] = {
                "score": category_score,
                "max_score": category_max_score,
                "percentage": round(category_percentage, 2),
                "weight": category["weight"]
            }

            total_score += category_score
            total_max_score += category_max_score

        # Calculate overall percentage
        overall_percentage = (total_score / total_max_score * 100) if total_max_score > 0 else 0

        # Determine risk level
        risk_level = self._determine_risk_level(overall_percentage)

        # Determine audit recommendation
        audit_recommendation = self._determine_audit_recommendation(overall_percentage, category_scores)

        return {
            "total_score": total_score,
            "max_score": total_max_score,
            "percentage": round(overall_percentage, 2),
            "risk_level": risk_level,
            "audit_recommendation": audit_recommendation,
            "category_scores": category_scores
        }

    def _determine_risk_level(self, percentage: float) -> Dict[str, str]:
        """Determine risk level based on overall score percentage"""
        if percentage >= 80:
            return {
                "level": "LOW",
                "fr": "Risque Faible",
                "en": "Low Risk",
                "color": "#10b981"  # Green
            }
        elif percentage >= 60:
            return {
                "level": "MEDIUM",
                "fr": "Risque Modéré",
                "en": "Medium Risk",
                "color": "#f59e0b"  # Orange
            }
        elif percentage >= 40:
            return {
                "level": "HIGH",
                "fr": "Risque Élevé",
                "en": "High Risk",
                "color": "#ef4444"  # Red
            }
        else:
            return {
                "level": "CRITICAL",
                "fr": "Risque Critique",
                "en": "Critical Risk",
                "color": "#dc2626"  # Dark red
            }

    def _determine_audit_recommendation(self, percentage: float, category_scores: Dict) -> Dict[str, str]:
        """Determine if a full audit is recommended"""
        critical_categories = []

        # Check for critical categories (< 50%)
        for cat_id, scores in category_scores.items():
            if scores["percentage"] < 50:
                critical_categories.append(cat_id)

        if percentage < 50 or len(critical_categories) >= 3:
            return {
                "recommendation": "FULL_AUDIT_REQUIRED",
                "fr": "Audit Complet Requis",
                "en": "Full Audit Required",
                "priority": "HIGH"
            }
        elif percentage < 70 or len(critical_categories) >= 1:
            return {
                "recommendation": "TARGETED_AUDIT_RECOMMENDED",
                "fr": "Audit Ciblé Recommandé",
                "en": "Targeted Audit Recommended",
                "priority": "MEDIUM"
            }
        else:
            return {
                "recommendation": "LIGHT_REVIEW",
                "fr": "Revue Légère Suffisante",
                "en": "Light Review Sufficient",
                "priority": "LOW"
            }

    def get_recommendations(self, responses: Dict[str, int], lang: str = "fr") -> List[Dict]:
        """
        Generate specific recommendations based on low-scoring areas
        """
        recommendations = []

        for category in self.questions_data["categories"]:
            for question in category["questions"]:
                question_id = question["id"]

                if question_id in responses:
                    user_value = responses[question_id]
                    max_value = max(opt["value"] for opt in question["options"])

                    # If user scored less than 50% on this question
                    if user_value < (max_value * 0.5):
                        recommendations.append({
                            "question_id": question_id,
                            "category": category["name"][lang],
                            "question": question["text"][lang],
                            "standard": question["standard"],
                            "severity": "high" if user_value == 0 else "medium"
                        })

        return recommendations
