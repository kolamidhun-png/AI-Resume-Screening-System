import os
import tempfile

import streamlit as st
import pandas as pd

from src.pdf_extractor import extract_text_from_pdf
from src.text_preprocessor import preprocess_text
from src.skill_extractor import extract_skills
from src.tfidf_matcher import calculate_similarity
from src.bert_matcher import calculate_bert_similarity
from src.ranking import calculate_final_score, get_candidate_category


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .score-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
        background-color: #ffffff;
    }

    .score-number {
        font-size: 30px;
        font-weight: 700;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .skill {
        display: inline-block;
        padding: 7px 12px;
        margin: 5px;
        border-radius: 20px;
        background-color: #e8f5e9;
        border: 1px solid #b7dfb9;
    }

    .missing-skill {
        display: inline-block;
        padding: 7px 12px;
        margin: 5px;
        border-radius: 20px;
        background-color: #ffebee;
        border: 1px solid #efb5bd;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Resume Screening System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent Resume–Job Matching using NLP, TF-IDF and BERT'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Screening System")

    st.write(
        """
        This system evaluates a candidate resume against
        a job description using multiple NLP techniques.
        """
    )

    st.divider()

    st.subheader("🧠 Technologies")

    st.write("• Python")
    st.write("• Streamlit")
    st.write("• NLP")
    st.write("• TF-IDF")
    st.write("• BERT")
    st.write("• Scikit-learn")
    st.write("• Sentence Transformers")

    st.divider()

    st.caption("AI Resume Screening System")
    st.caption("B.Tech AI/ML Project")


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">📄 Candidate Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        help="Upload the candidate's resume in PDF format."
    )


with col2:

    job_description = st.text_area(
        "💼 Job Description",
        height=220,
        placeholder=(
            "Paste the complete job description here...\n\n"
            "Example: Python, Machine Learning, SQL, "
            "Data Structures, Git..."
        )
    )


st.write("")


screen_button = st.button(
    "🔍 Screen Resume",
    use_container_width=True,
    type="primary"
)


# ---------------------------------------------------------
# SCREENING PROCESS
# ---------------------------------------------------------

if screen_button:

    if uploaded_file is None:

        st.warning("⚠️ Please upload a resume PDF.")

    elif not job_description.strip():

        st.warning("⚠️ Please enter a job description.")

    else:

        temp_path = None

        try:

            with st.spinner(
                "🤖 AI is analyzing the resume..."
            ):

                # -------------------------------------------------
                # SAVE TEMPORARY PDF
                # -------------------------------------------------

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_file:

                    temp_file.write(
                        uploaded_file.getbuffer()
                    )

                    temp_path = temp_file.name


                # -------------------------------------------------
                # STEP 1 — PDF TEXT EXTRACTION
                # -------------------------------------------------

                resume_text = extract_text_from_pdf(
                    temp_path
                )


                if not resume_text:

                    st.error(
                        "❌ Could not extract text from the PDF."
                    )

                    st.stop()


                # -------------------------------------------------
                # STEP 2 — TEXT PREPROCESSING
                # -------------------------------------------------

                clean_resume = preprocess_text(
                    resume_text
                )

                clean_job = preprocess_text(
                    job_description
                )


                # -------------------------------------------------
                # STEP 3 — SKILL EXTRACTION
                # -------------------------------------------------

                resume_skills = extract_skills(
                    clean_resume
                )

                job_skills = extract_skills(
                    clean_job
                )


                # -------------------------------------------------
                # STEP 4 — SKILL MATCHING
                # -------------------------------------------------

                if job_skills:

                    matched_skills = [
                        skill
                        for skill in job_skills
                        if skill in resume_skills
                    ]

                    missing_skills = [
                        skill
                        for skill in job_skills
                        if skill not in resume_skills
                    ]

                    skill_score = (
                        len(matched_skills)
                        / len(job_skills)
                    ) * 100

                else:

                    matched_skills = []

                    missing_skills = []

                    skill_score = 0


                # -------------------------------------------------
                # STEP 5 — TF-IDF MATCHING
                # -------------------------------------------------

                tfidf_score = (
                    calculate_similarity(
                        clean_resume,
                        clean_job
                    ) * 100
                )


                # -------------------------------------------------
                # STEP 6 — BERT MATCHING
                # -------------------------------------------------

                bert_score = (
                    calculate_bert_similarity(
                        clean_resume,
                        clean_job
                    ) * 100
                )

                bert_score = min(
                    max(bert_score, 0),
                    100
                )


                # -------------------------------------------------
                # STEP 7 — FINAL SCORE
                # -------------------------------------------------

                final_score = calculate_final_score(
                    skill_score,
                    tfidf_score,
                    bert_score
                )


                # -------------------------------------------------
                # STEP 8 — RECOMMENDATION
                # -------------------------------------------------

                category = get_candidate_category(
                    final_score
                )


            # -----------------------------------------------------
            # SUCCESS MESSAGE
            # -----------------------------------------------------

            st.success(
                "✅ Resume screening completed successfully!"
            )


            # -----------------------------------------------------
            # SCORE DASHBOARD
            # -----------------------------------------------------

            st.markdown(
                '<div class="section-title">📊 Screening Results</div>',
                unsafe_allow_html=True
            )


            col1, col2, col3, col4 = st.columns(4)


            with col1:

                st.metric(
                    "🧠 Skill Match",
                    f"{skill_score:.1f}%"
                )


            with col2:

                st.metric(
                    "📚 TF-IDF",
                    f"{tfidf_score:.1f}%"
                )


            with col3:

                st.metric(
                    "🤖 BERT",
                    f"{bert_score:.1f}%"
                )


            with col4:

                st.metric(
                    "⭐ Final Score",
                    f"{final_score:.1f}%"
                )


            # -----------------------------------------------------
            # FINAL RECOMMENDATION
            # -----------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '🎯 Candidate Recommendation'
                '</div>',
                unsafe_allow_html=True
            )


            if final_score >= 80:

                st.success(
                    f"🟢 {category}"
                )

            elif final_score >= 65:

                st.info(
                    f"🔵 {category}"
                )

            elif final_score >= 50:

                st.warning(
                    f"🟡 {category}"
                )

            else:

                st.error(
                    f"🔴 {category}"
                )


            # -----------------------------------------------------
            # SCORE CHART
            # -----------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '📈 Model Performance'
                '</div>',
                unsafe_allow_html=True
            )


            chart_data = pd.DataFrame(
                {
                    "Method": [
                        "Skill Match",
                        "TF-IDF",
                        "BERT",
                        "Final Score"
                    ],
                    "Score": [
                        skill_score,
                        tfidf_score,
                        bert_score,
                        final_score
                    ]
                }
            )

            st.bar_chart(
                chart_data.set_index("Method")
            )


            # -----------------------------------------------------
            # SKILLS
            # -----------------------------------------------------

            col1, col2 = st.columns(2)


            with col1:

                st.markdown(
                    '<div class="section-title">'
                    '✅ Matched Skills'
                    '</div>',
                    unsafe_allow_html=True
                )

                if matched_skills:

                    for skill in matched_skills:

                        st.markdown(
                            f'<span class="skill">✓ {skill}</span>',
                            unsafe_allow_html=True
                        )

                else:

                    st.write(
                        "No matching skills found."
                    )


            with col2:

                st.markdown(
                    '<div class="section-title">'
                    '❌ Missing Skills'
                    '</div>',
                    unsafe_allow_html=True
                )

                if missing_skills:

                    for skill in missing_skills:

                        st.markdown(
                            f'<span class="missing-skill">'
                            f'✗ {skill}'
                            f'</span>',
                            unsafe_allow_html=True
                        )

                else:

                    st.write(
                        "No major missing skills detected."
                    )


            # -----------------------------------------------------
            # RESUME DETAILS
            # -----------------------------------------------------

            st.markdown(
                '<div class="section-title">'
                '📄 Resume Details'
                '</div>',
                unsafe_allow_html=True
            )


            with st.expander(
                "View Extracted Resume Text"
            ):

                st.text(
                    resume_text
                )


            with st.expander(
                "View Detected Resume Skills"
            ):

                if resume_skills:

                    st.write(
                        ", ".join(resume_skills)
                    )

                else:

                    st.write(
                        "No predefined skills detected."
                    )


        except Exception as e:

            st.error(
                "❌ An error occurred while processing the resume."
            )

            st.exception(e)


        finally:

            if (
                temp_path
                and os.path.exists(temp_path)
            ):

                os.remove(temp_path)