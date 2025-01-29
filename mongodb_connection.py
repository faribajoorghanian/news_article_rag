from pymongo import MongoClient
from pymongo.server_api import ServerApi
from embedding import get_embedding
import json

# MongoDB URI and setup: you should use your own username and password
uri = "mongodb+srv://user:pass@cluster0.ctq0t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new MongoClient and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Confirm the connection
def test_connection():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error: {e}")

# Database and collection setup
db = client["ag_news_db"]
collection = db["articles"]

# Function to store embeddings in MongoDB
def store_embeddings(texts, collection):
    """
    Store the embeddings and corresponding text in MongoDB collection.
    
    Args:
    - texts: List of article texts.
    - collection: MongoDB collection where the data will be stored.
    """
    for text in texts:
        embedding = get_embedding(text)
        
        document_data = {
            "text": text,
            "embedding": embedding
        }
        
        collection.insert_one(document_data)

# Function to print the vector index configuration
def print_vector_index_config():
    """
    Prints the vector index configuration for MongoDB Atlas Search manually.
    """
    vector_index_config = {
        "fields": [
            {
                "numDimensions": 384,
                "path": "embedding",
                "similarity": "cosine",
                "type": "vector"
            }
        ]
    }
    
    # Print the vector index configuration in JSON format
    print("Vector Index Configuration should be copied and created manually in MongoDB website< Atlas serach< choose the cluster< Create a Search Index< JSON Editor< copy and paste the vector index bellow. you should choose the correct Database and Collection.):")
    print(json.dumps(vector_index_config, indent=2))

# Function to manually create a vector index in MongoDB Atlas (print configuration only)
def create_manual_vector_index():
    """
    Prints the vector index configuration for manual setup in MongoDB Atlas.
    """
    print_vector_index_config()



