import numpy as np
from embedding import get_embedding

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.
    
    Args:
    - vec1: First vector.
    - vec2: Second vector.
    
    Returns:
    - similarity: Cosine similarity score between the two vectors.
    """
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

# Perform vector search using cosine similarity
def vector_search(query, collection):
    """
    Perform a vector search based on the query in the MongoDB collection.
    
    Args:
    - query: Query string for searching.
    - collection: MongoDB collection containing the stored embeddings.
    
    Returns:
    - results: List of top matching articles from the collection.
    """
    # Get the embedding for the query
    query_embedding = get_embedding(query)
    
    # MongoDB aggregation pipeline for searching
    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",  # The vector index created in MongoDB
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 150,  # Number of candidates to consider
                "limit": 4  # Limit to top 4 results
            }
        },
        {
            "$project": {
                "text": 1,  # Return the article text
                "score": {"$meta": "vectorSearchScore"}  # Return the similarity score
            }
        }
    ]
    
    # Execute the pipeline and get results
    results = collection.aggregate(pipeline)
    
    # Convert to list for easy handling
    return list(results)
