from src.text_preprocessor import preprocess_text
from src.skill_extractor import extract_skills
from src.tfidf_matcher import calculate_similarity
from src.ranking import calculate_final_score


def test_text_preprocessing():
    text = "Python Developer!"
    result = preprocess_text(text)

    assert "python" in result
    assert "developer" in result


def test_skill_extraction():
    text = "Python developer with SQL and Machine Learning experience."

    skills = extract_skills(text)

    assert "python" in skills
    assert "sql" in skills
    assert "machine learning" in skills


def test_tfidf_similarity():
    resume = "Python developer with machine learning and SQL experience."

    job = "Looking for Python developer with machine learning and SQL skills."

    score = calculate_similarity(resume, job)

    assert 0 <= score <= 1
    assert score > 0


def test_final_score():
    score = calculate_final_score(
        skill_score=100,
        tfidf_score=65,
        bert_score=79
    )

    assert 0 <= score <= 100
    assert round(score, 2) == 83.90