from mongodb_connection import test_connection, store_embeddings, create_manual_vector_index, collection
from data_loader import load_ag_news, preprocess_data
from vector_search import vector_search

def setup_database():
    """
    Set up the MongoDB database, store embeddings, and create the vector index.
    This function will be run once to prepare the data in MongoDB.
    """
    # Test MongoDB connection
    test_connection()

    # Load and preprocess the dataset
    dataset = load_ag_news()
    texts = preprocess_data(dataset)

    # Store the embeddings in MongoDB
    store_embeddings(texts, collection)
    print("Embeddings stored successfully!")

    # Create the vector index in MongoDB
    create_manual_vector_index()

def perform_search(query):
    """
    Perform a vector search with the given query.
    
    Args:
    - query: The search query string.
    """
    # Perform vector search
    results = vector_search(query, collection)

    # Print the top 4 most relevant articles
    for result in results:
        print(f"Text: {result['text']} | Similarity Score: {result['score']}")

if __name__ == "__main__":
    # Step 1: Set up the database (embedding + index creation)
    # Uncomment this line to run it once and store the embeddings and vector index
    setup_database()  # Run this only once to store the embeddings and create the vector index
    
    # Step 2: Now perform a search (after embeddings and vector index are created)
    # Example search query
    query = "Latest advancements in technology"
    perform_search(query)
