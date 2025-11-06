# Security Assessment Tool

Professional security questionnaire for auditing web applications and infrastructure.

## 🔗 Live Demo

**Try it now:** https://app-security-audit.streamlit.app/

No installation required - start evaluating applications immediately.

---

## What is this?

A comprehensive security assessment tool based on industry standards:
- OWASP Top 10
- ISO 27001
- ANSSI recommendations

**Purpose:** Quickly evaluate 800+ applications and identify those requiring full security audits.

---

## Features

- **39 security questions** across 7 categories
- **Automatic scoring** with risk levels (Low/Medium/High/Critical)
- **Personalized recommendations** based on identified weaknesses
- **Excel export** (templates + detailed reports)
- **Multi-language** support (French/English)
- **Modern interface** with real-time progress tracking

---

## Quick Start

### Option 1: Use Online (Recommended)

Visit https://app-security-audit.streamlit.app/ - that's it!

### Option 2: Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Security Categories

1. **Identity & Access Management** (IAM) - 20%
2. **Network Architecture** - 18%
3. **Flows & Interconnections** - 15%
4. **Hosting & Infrastructure** - 17%
5. **Data Security** - 18%
6. **Application Security** - 20%
7. **Logging & Monitoring** - 12%

---

## Scoring

| Score | Risk Level | Action |
|-------|------------|--------|
| 80-100% | Low | Light review |
| 60-79% | Medium | Targeted audit |
| 40-59% | High | Targeted audit |
| 0-39% | Critical | Full audit required |

---

## Workflow for 800 Applications

1. **Download** Excel template from the app
2. **Distribute** to application owners
3. **Collect** completed questionnaires
4. **Import** responses (manually or via API)
5. **Generate** reports with scores
6. **Prioritize** audits based on risk levels

---

## Two Versions Available

### Streamlit (Current)
- ✅ Fast deployment (5 minutes)
- ✅ Free hosting on Streamlit Cloud
- ✅ Zero configuration
- ✅ Perfect for POC and audits

### React + Flask (Alternative)
- ✅ Production-ready
- ✅ Scalable architecture
- ✅ Full customization
- ✅ REST API included

See `VERSION_COMPARISON.md` for details.

---

## Documentation

- `QUICKSTART_STREAMLIT.md` - 5-minute quick start
- `STREAMLIT_DEPLOYMENT.md` - Deployment guide
- `ROADMAP.md` - Future improvements
- `QUICK_FIX_SLEEP.md` - Fix app sleep issue (free tier)

---

## Project Structure

```
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── streamlit_app/
│   ├── data/
│   │   └── questions.json   # Security questions (FR/EN)
│   └── utils/
│       ├── questionnaire.py # Scoring engine
│       ├── excel_export.py  # Excel generation
│       └── translations.py  # Multi-language
└── .streamlit/
    └── config.toml          # Theme configuration
```

---

## Tech Stack

**Backend:** Python 3.8+, Streamlit
**Export:** openpyxl
**Hosting:** Streamlit Cloud (free tier)

---

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## Roadmap

See `ROADMAP.md` for detailed improvement plans.

**Priority items:**
- Add 40-50 more questions
- Bulk Excel import
- Multi-app dashboard
- New categories (Cloud, DevSecOps, Compliance)

---

## Support

- **Issues:** Open an issue on GitHub
- **Documentation:** Check the `/docs` folder
- **Live App:** https://app-security-audit.streamlit.app/

---

## License

Internal security audit tool - Professional use

---

## Standards References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [ANSSI](https://www.ssi.gouv.fr/)

---

**Built with [Claude Code](https://claude.com/claude-code)**
