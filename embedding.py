from sentence_transformers import SentenceTransformer

# Initialize the Sentence Transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_embedding(text: str):
    """
    Convert a sentence to embedding using the SentenceTransformer model.
    
    Args:
    - text: A string sentence to convert to embedding.
    
    Returns:
    - embedding: List of embedding values (float list)
    """
    return model.encode(text).tolist()
