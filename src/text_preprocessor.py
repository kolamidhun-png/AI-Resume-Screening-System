import re


def preprocess_text(text):
    """
    Clean and normalize resume or job-description text.
    """
    text = text.lower()

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Replace special characters with spaces
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()