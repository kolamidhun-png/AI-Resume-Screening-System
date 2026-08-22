# Models

The AI Resume Screening System uses a pretrained Sentence Transformer model for semantic resume-job matching.

## BERT-Based Model

Model used:

`all-MiniLM-L6-v2`

The model converts resume and job-description text into numerical sentence embeddings. Cosine similarity is then used to measure semantic similarity.

The pretrained model is downloaded automatically through the Sentence Transformers library when required.

The model files are not stored directly in this repository.