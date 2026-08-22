def calculate_final_score(skill_score, tfidf_score, bert_score):
    """
    Calculate the final resume screening score.

    skill_score, tfidf_score and bert_score
    should be provided as percentages from 0 to 100.
    """

    final_score = (
        (skill_score * 0.40)
        + (tfidf_score * 0.25)
        + (bert_score * 0.35)
    )

    return round(final_score, 2)


def get_candidate_category(score):
    """
    Categorize a candidate based on the final screening score.
    """

    if score >= 80:
        return "Highly Recommended"
    elif score >= 65:
        return "Recommended"
    elif score >= 50:
        return "Potential Candidate"
    else:
        return "Not Recommended"