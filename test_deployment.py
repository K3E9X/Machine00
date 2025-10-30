"""
Test script to verify Streamlit application is ready for deployment
"""
import sys
from pathlib import Path

def test_file_structure():
    """Check all required files exist"""
    print("Testing file structure...")

    required_files = [
        'app.py',
        'requirements.txt',
        '.streamlit/config.toml',
        'streamlit_app/__init__.py',
        'streamlit_app/utils/__init__.py',
        'streamlit_app/utils/questionnaire.py',
        'streamlit_app/utils/excel_export.py',
        'streamlit_app/utils/translations.py',
        'streamlit_app/data/questions.json',
    ]

    all_exist = True
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} MISSING")
            all_exist = False

    return all_exist

def test_imports():
    """Test all custom imports work"""
    print("\nTesting imports...")

    try:
        from streamlit_app.utils.questionnaire import QuestionnaireModel
        print("  ✓ QuestionnaireModel")
    except Exception as e:
        print(f"  ✗ QuestionnaireModel: {e}")
        return False

    try:
        from streamlit_app.utils.excel_export import ExcelExportService
        print("  ✓ ExcelExportService")
    except Exception as e:
        print(f"  ✗ ExcelExportService: {e}")
        return False

    try:
        from streamlit_app.utils.translations import get_text
        print("  ✓ translations")
    except Exception as e:
        print(f"  ✗ translations: {e}")
        return False

    return True

def test_questionnaire():
    """Test questionnaire functionality"""
    print("\nTesting questionnaire functionality...")

    try:
        from streamlit_app.utils.questionnaire import QuestionnaireModel

        model = QuestionnaireModel()

        # Test loading questions
        data_fr = model.get_all_questions('fr')
        data_en = model.get_all_questions('en')

        print(f"  ✓ Questions loaded: {len(data_fr['categories'])} categories")

        # Test scoring
        test_responses = {
            'iam_001': 10,
            'iam_002': 7,
            'net_001': 8,
        }

        score = model.calculate_score(test_responses)
        print(f"  ✓ Scoring works: {score['percentage']:.2f}%")
        print(f"    Risk level: {score['risk_level']['fr']}")
        print(f"    Recommendation: {score['audit_recommendation']['fr']}")

        # Test recommendations
        recommendations = model.get_recommendations(test_responses, 'fr')
        print(f"  ✓ Recommendations: {len(recommendations)} items")

        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_translations():
    """Test translation system"""
    print("\nTesting translations...")

    try:
        from streamlit_app.utils.translations import get_text

        # Test French
        text_fr = get_text('app_title', 'fr')
        print(f"  ✓ French: {text_fr}")

        # Test English
        text_en = get_text('app_title', 'en')
        print(f"  ✓ English: {text_en}")

        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def test_requirements():
    """Check requirements.txt is valid"""
    print("\nTesting requirements.txt...")

    try:
        with open('requirements.txt', 'r') as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]

        print(f"  ✓ {len(lines)} packages listed")
        for line in lines:
            print(f"    - {line}")

        # Check essential packages
        content = ' '.join(lines)
        if 'streamlit' in content:
            print("  ✓ streamlit included")
        else:
            print("  ✗ streamlit MISSING")
            return False

        if 'openpyxl' in content:
            print("  ✓ openpyxl included")
        else:
            print("  ✗ openpyxl MISSING")
            return False

        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def test_app_syntax():
    """Test app.py syntax"""
    print("\nTesting app.py syntax...")

    try:
        import py_compile
        py_compile.compile('app.py', doraise=True)
        print("  ✓ app.py syntax valid")
        return True
    except Exception as e:
        print(f"  ✗ Syntax error: {e}")
        return False

def main():
    print("=" * 60)
    print("STREAMLIT APPLICATION DEPLOYMENT READINESS TEST")
    print("=" * 60)

    tests = [
        ("File Structure", test_file_structure),
        ("Imports", test_imports),
        ("Questionnaire", test_questionnaire),
        ("Translations", test_translations),
        ("Requirements", test_requirements),
        ("App Syntax", test_app_syntax),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ {name} failed with exception: {e}")
            results.append((name, False))
        print()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    all_passed = True
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:10} {name}")
        if not result:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n✅ APPLICATION IS READY FOR STREAMLIT CLOUD DEPLOYMENT!")
        print("\nNext steps:")
        print("1. Push to GitHub")
        print("2. Go to https://share.streamlit.io/")
        print("3. Connect your repository")
        print("4. Deploy app.py")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED - Please fix issues before deployment")
        return 1

if __name__ == "__main__":
    sys.exit(main())
