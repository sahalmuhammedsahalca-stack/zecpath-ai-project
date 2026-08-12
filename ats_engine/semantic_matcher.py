from sentence_transformers import SentenceTransformer, util

# Load the pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_similarity(resume_text, jd_text):
    """
    Calculates semantic similarity between
    resume and job description.
    """

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    jd_embedding = model.encode(
        jd_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        resume_embedding,
        jd_embedding
    )

    score = round(float(similarity[0][0]) * 100, 2)

    return {
        "semantic_score": score
    }