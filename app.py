import streamlit as st
from streamlit_app.utils.questionnaire import QuestionnaireModel
from streamlit_app.utils.excel_export import ExcelExportService
from streamlit_app.utils.translations import get_text
from datetime import datetime
import io

# Page config
st.set_page_config(
    page_title="Security Assessment Tool",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1F4E78 0%, #4A90E2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .risk-badge {
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
    }
    .category-progress {
        background: #e5e7eb;
        border-radius: 4px;
        height: 8px;
        margin: 0.5rem 0;
    }
    .progress-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.3s;
    }
    .question-card {
        background: #f9fafb;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #1F4E78;
        margin: 1rem 0;
    }
    .standard-tag {
        background: #e5e7eb;
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        font-size: 0.75rem;
        margin: 0.25rem;
        display: inline-block;
    }
    div[data-testid="stButton"] button {
        background: #1F4E78;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
    }
    div[data-testid="stButton"] button:hover {
        background: #173a5a;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'lang' not in st.session_state:
    st.session_state.lang = 'fr'
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'app_info' not in st.session_state:
    st.session_state.app_info = {
        'name': '',
        'owner': '',
        'contact': '',
        'environment': 'Production',
        'description': ''
    }
if 'results' not in st.session_state:
    st.session_state.results = None

# Initialize models
@st.cache_resource
def get_questionnaire_model():
    return QuestionnaireModel()

questionnaire = get_questionnaire_model()


def render_header():
    """Render the application header"""
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"""
        <div class="main-header">
            <h1>{get_text('app_title', st.session_state.lang)}</h1>
            <p>{get_text('app_subtitle', st.session_state.lang)}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🌐 FR/EN", key="lang_toggle"):
            st.session_state.lang = 'en' if st.session_state.lang == 'fr' else 'fr'
            st.rerun()


def render_home():
    """Render home page"""
    render_header()

    st.markdown(f"## {get_text('home_welcome', st.session_state.lang)}")
    st.markdown(f"{get_text('home_description', st.session_state.lang)}")

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"▶️ {get_text('home_start', st.session_state.lang)}", use_container_width=True):
            st.session_state.page = 'questionnaire'
            st.session_state.responses = {}
            st.session_state.results = None
            st.rerun()

    with col2:
        if st.button(f"📥 {get_text('home_template', st.session_state.lang)}", use_container_width=True):
            download_template()

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(f"### {get_text('home_features_title', st.session_state.lang)}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">✅</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature1', st.session_state.lang)), unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">📊</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature2', st.session_state.lang)), unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">💡</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature3', st.session_state.lang)), unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">📋</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature4', st.session_state.lang)), unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">🌍</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature5', st.session_state.lang)), unsafe_allow_html=True)

        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 2rem;">⚡</div>
            <p>{}</p>
        </div>
        """.format(get_text('home_feature6', st.session_state.lang)), unsafe_allow_html=True)


def download_template():
    """Generate and download Excel template"""
    excel_service = ExcelExportService(questionnaire.questions_data)
    wb = excel_service.create_questionnaire_template(
        lang=st.session_state.lang,
        app_name=st.session_state.app_info.get('name', None)
    )

    # Save to BytesIO
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    filename = f"security_questionnaire_{st.session_state.lang}_{datetime.now().strftime('%Y%m%d')}.xlsx"

    st.download_button(
        label=f"💾 {get_text('home_template', st.session_state.lang)}",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def render_questionnaire():
    """Render questionnaire page"""
    render_header()

    if st.button(f"← {get_text('back', st.session_state.lang)}"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown(f"## {get_text('quest_title', st.session_state.lang)}")

    # Calculate progress
    questions_data = questionnaire.get_all_questions(st.session_state.lang)
    total_questions = sum(len(cat['questions']) for cat in questions_data['categories'])
    answered_questions = len(st.session_state.responses)
    progress = (answered_questions / total_questions * 100) if total_questions > 0 else 0

    st.markdown(f"**{get_text('quest_progress', st.session_state.lang)}:** {answered_questions}/{total_questions} ({progress:.0f}%)")
    st.progress(progress / 100)

    st.markdown("<br>", unsafe_allow_html=True)

    # Application info
    with st.expander(f"📋 {get_text('quest_app_info', st.session_state.lang)}", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.app_info['name'] = st.text_input(
                get_text('quest_app_name', st.session_state.lang),
                value=st.session_state.app_info.get('name', ''),
                placeholder=get_text('quest_app_name_placeholder', st.session_state.lang)
            )
            st.session_state.app_info['owner'] = st.text_input(
                get_text('quest_owner', st.session_state.lang),
                value=st.session_state.app_info.get('owner', ''),
                placeholder=get_text('quest_owner_placeholder', st.session_state.lang)
            )
        with col2:
            st.session_state.app_info['contact'] = st.text_input(
                get_text('quest_contact', st.session_state.lang),
                value=st.session_state.app_info.get('contact', ''),
                placeholder=get_text('quest_contact_placeholder', st.session_state.lang)
            )
            st.session_state.app_info['environment'] = st.selectbox(
                get_text('quest_environment', st.session_state.lang),
                ['Production', 'Staging', 'Development'],
                index=['Production', 'Staging', 'Development'].index(
                    st.session_state.app_info.get('environment', 'Production')
                )
            )

        st.session_state.app_info['description'] = st.text_area(
            get_text('quest_description', st.session_state.lang),
            value=st.session_state.app_info.get('description', ''),
            placeholder=get_text('quest_description_placeholder', st.session_state.lang)
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Categories tabs
    category_names = [cat['name'][st.session_state.lang] for cat in questions_data['categories']]
    tabs = st.tabs(category_names)

    for idx, (tab, category) in enumerate(zip(tabs, questions_data['categories'])):
        with tab:
            render_category_questions(category)

    st.markdown("<br>", unsafe_allow_html=True)

    # Submit button
    if progress == 100:
        if st.button(f"✅ {get_text('quest_submit', st.session_state.lang)}", use_container_width=True):
            # Calculate results
            score_data = questionnaire.calculate_score(st.session_state.responses)
            recommendations = questionnaire.get_recommendations(
                st.session_state.responses,
                st.session_state.lang
            )

            st.session_state.results = {
                'score': score_data,
                'recommendations': recommendations,
                'app_info': st.session_state.app_info.copy(),
                'responses': st.session_state.responses.copy()
            }

            st.session_state.page = 'results'
            st.rerun()
    else:
        st.warning(get_text('quest_required', st.session_state.lang))


def render_category_questions(category):
    """Render questions for a category"""
    lang = st.session_state.lang

    for idx, question in enumerate(category['questions']):
        st.markdown(f"""
        <div class="question-card">
            <strong>Q{idx + 1}.</strong> {question['text'][lang]}
            <br>
            <div style="margin-top: 0.5rem;">
        """, unsafe_allow_html=True)

        # Standards tags
        for standard in question['standard']:
            st.markdown(f'<span class="standard-tag">{standard}</span>', unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)

        # Options
        options = {opt['label'][lang]: opt['value'] for opt in question['options']}

        # Find current selection
        current_value = st.session_state.responses.get(question['id'])
        current_label = None
        if current_value is not None:
            for opt in question['options']:
                if opt['value'] == current_value:
                    current_label = opt['label'][lang]
                    break

        selected = st.radio(
            get_text('quest_select', st.session_state.lang),
            options=list(options.keys()),
            index=list(options.keys()).index(current_label) if current_label else None,
            key=f"question_{question['id']}",
            label_visibility="collapsed"
        )

        if selected:
            st.session_state.responses[question['id']] = options[selected]

        st.markdown("<br>", unsafe_allow_html=True)


def render_results():
    """Render results page"""
    render_header()

    if st.session_state.results is None:
        st.error("No results available")
        if st.button(get_text('back', st.session_state.lang)):
            st.session_state.page = 'home'
            st.rerun()
        return

    results = st.session_state.results
    score = results['score']
    lang = st.session_state.lang

    # Action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(f"← {get_text('back', lang)}"):
            st.session_state.page = 'home'
            st.rerun()
    with col2:
        if st.button(f"🔄 {get_text('results_new_assessment', lang)}"):
            st.session_state.page = 'questionnaire'
            st.session_state.responses = {}
            st.session_state.results = None
            st.rerun()
    with col3:
        download_results_excel()

    st.markdown(f"## {get_text('results_title', lang)}")

    if results['app_info'].get('name'):
        st.markdown(f"**{results['app_info']['name']}**")

    st.markdown("<br>", unsafe_allow_html=True)

    # Score summary
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"### {get_text('results_overall_score', lang)}")
        st.markdown(f"""
        <div style="font-size: 3rem; font-weight: 700; color: {score['risk_level']['color']};">
            {score['percentage']}%
        </div>
        <div style="color: #6b7280;">
            {score['total_score']} / {score['max_score']} points
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"### {get_text('results_risk_level', lang)}")
        st.markdown(f"""
        <div class="risk-badge" style="background: {score['risk_level']['color']}; color: white;">
            {score['risk_level'][lang]}
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"### {get_text('results_recommendation', lang)}")
        priority_colors = {'HIGH': '#ef4444', 'MEDIUM': '#f59e0b', 'LOW': '#10b981'}
        color = priority_colors.get(score['audit_recommendation']['priority'], '#6b7280')
        st.markdown(f"""
        <div class="risk-badge" style="background: {color}; color: white;">
            {score['audit_recommendation'][lang]}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Category breakdown
    st.markdown(f"### {get_text('results_category_breakdown', lang)}")

    # Get category names
    questions_data = questionnaire.get_all_questions(lang)
    category_names = {cat['id']: cat['name'][lang] for cat in questions_data['categories']}

    for cat_id, cat_score in score['category_scores'].items():
        cat_name = category_names.get(cat_id, cat_id)
        percentage = cat_score['percentage']

        # Determine color
        if percentage >= 80:
            color = '#10b981'
        elif percentage >= 60:
            color = '#f59e0b'
        elif percentage >= 40:
            color = '#ef4444'
        else:
            color = '#dc2626'

        st.markdown(f"**{cat_name}**: {percentage}% ({cat_score['score']}/{cat_score['max_score']})")
        st.markdown(f"""
        <div class="category-progress">
            <div class="progress-fill" style="width: {percentage}%; background: {color};"></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Recommendations
    if results['recommendations']:
        st.markdown(f"### {get_text('results_recommendations', lang)}")

        for rec in results['recommendations']:
            severity_color = '#ef4444' if rec['severity'] == 'high' else '#f59e0b'
            severity_text = get_text('results_high', lang) if rec['severity'] == 'high' else get_text('results_medium', lang)

            st.markdown(f"""
            <div class="question-card">
                <span class="risk-badge" style="background: {severity_color}; color: white; font-size: 0.75rem;">
                    {severity_text}
                </span>
                <strong style="margin-left: 0.5rem;">{rec['category']}</strong>
                <p style="margin: 0.5rem 0;">{rec['question']}</p>
                <div>
                    <span style="font-size: 0.875rem; color: #6b7280;">{get_text('quest_standards', lang)}:</span>
            """, unsafe_allow_html=True)

            for std in rec['standard']:
                st.markdown(f'<span class="standard-tag">{std}</span>', unsafe_allow_html=True)

            st.markdown("</div></div>", unsafe_allow_html=True)
    else:
        st.success(get_text('results_no_recommendations', lang))


def download_results_excel():
    """Generate and download results Excel"""
    if st.session_state.results is None:
        return

    excel_service = ExcelExportService(questionnaire.questions_data)
    wb = excel_service.create_results_report(
        st.session_state.results['responses'],
        st.session_state.results['score'],
        st.session_state.results['recommendations'],
        st.session_state.lang,
        st.session_state.results['app_info']
    )

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    app_name = st.session_state.results['app_info'].get('name', 'application')
    filename = f"security_assessment_{app_name}_{datetime.now().strftime('%Y%m%d')}.xlsx"

    st.download_button(
        label=f"📥 {get_text('results_export', st.session_state.lang)}",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


# Main app
def main():
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'questionnaire':
        render_questionnaire()
    elif st.session_state.page == 'results':
        render_results()

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #6b7280; font-size: 0.875rem;'>"
        "Security Assessment Tool - Based on OWASP Top 10, ISO 27001, ANSSI"
        "</div>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
