from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_bert_similarity(resume_text, job_description):
    """
    Calculate semantic similarity between a resume
    and job description using BERT embeddings.
    """

    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_numpy=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    return float(similarity[0][0])