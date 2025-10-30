from flask import Blueprint, jsonify, request, send_file
from models.questionnaire import QuestionnaireModel
from services.excel_export import ExcelExportService
import io
from datetime import datetime

api = Blueprint('api', __name__)

# Initialize models
questionnaire_model = QuestionnaireModel()
excel_service = ExcelExportService(questionnaire_model.questions_data)


@api.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})


@api.route('/questions', methods=['GET'])
def get_questions():
    """Get all questions"""
    lang = request.args.get('lang', 'fr')

    if lang not in ['fr', 'en']:
        return jsonify({"error": "Invalid language. Use 'fr' or 'en'"}), 400

    questions = questionnaire_model.get_all_questions(lang)
    return jsonify(questions)


@api.route('/questions/<category_id>', methods=['GET'])
def get_category(category_id):
    """Get questions for a specific category"""
    lang = request.args.get('lang', 'fr')

    category = questionnaire_model.get_category(category_id, lang)

    if not category:
        return jsonify({"error": "Category not found"}), 404

    return jsonify(category)


@api.route('/submit', methods=['POST'])
def submit_questionnaire():
    """Submit questionnaire responses and get score"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    responses = data.get('responses', {})
    lang = data.get('lang', 'fr')
    app_info = data.get('app_info', {})

    if not responses:
        return jsonify({"error": "No responses provided"}), 400

    # Calculate score
    score_data = questionnaire_model.calculate_score(responses)

    # Get recommendations
    recommendations = questionnaire_model.get_recommendations(responses, lang)

    result = {
        "score": score_data,
        "recommendations": recommendations,
        "app_info": app_info,
        "timestamp": datetime.now().isoformat()
    }

    return jsonify(result)


@api.route('/export/template', methods=['GET'])
def export_template():
    """Export blank questionnaire template as Excel"""
    lang = request.args.get('lang', 'fr')
    app_name = request.args.get('app_name', None)

    if lang not in ['fr', 'en']:
        return jsonify({"error": "Invalid language. Use 'fr' or 'en'"}), 400

    # Create Excel workbook
    wb = excel_service.create_questionnaire_template(lang, app_name)

    # Save to BytesIO
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    filename = f"security_questionnaire_template_{lang}_{datetime.now().strftime('%Y%m%d')}.xlsx"

    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=filename
    )


@api.route('/export/results', methods=['POST'])
def export_results():
    """Export questionnaire results as Excel"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    responses = data.get('responses', {})
    lang = data.get('lang', 'fr')
    app_info = data.get('app_info', {})

    if not responses:
        return jsonify({"error": "No responses provided"}), 400

    # Calculate score and recommendations
    score_data = questionnaire_model.calculate_score(responses)
    recommendations = questionnaire_model.get_recommendations(responses, lang)

    # Create Excel report
    wb = excel_service.create_results_report(
        responses,
        score_data,
        recommendations,
        lang,
        app_info
    )

    # Save to BytesIO
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    app_name = app_info.get('name', 'application')
    filename = f"security_assessment_{app_name}_{datetime.now().strftime('%Y%m%d')}.xlsx"

    return send_file(
        output,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=filename
    )


@api.route('/stats', methods=['GET'])
def get_stats():
    """Get questionnaire statistics"""
    total_questions = 0
    categories_count = len(questionnaire_model.questions_data['categories'])

    for category in questionnaire_model.questions_data['categories']:
        total_questions += len(category['questions'])

    return jsonify({
        "total_questions": total_questions,
        "categories_count": categories_count,
        "categories": [
            {
                "id": cat['id'],
                "name": cat['name'],
                "questions_count": len(cat['questions']),
                "weight": cat['weight']
            }
            for cat in questionnaire_model.questions_data['categories']
        ]
    })
