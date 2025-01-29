# News Article Embedding and Vector Search with MongoDB

This project demonstrates how to generate text embeddings from news articles using the **SentenceTransformer** model and store them in **MongoDB** for efficient vector-based search. The project uses **cosine similarity** to search for articles similar to a given query.

## Prerequisites

Before you start, make sure you have:

- **MongoDB Atlas** account or a local MongoDB setup.
- **Python 3.7+** installed.
- The following Python libraries installed (see `requirements.txt` for the full list).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

2. **Set up the virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:
   - If you don’t have MongoDB set up yet, you can create a free MongoDB Atlas cluster or install MongoDB locally.
   - Create a new database named `ag_news_db` and a collection called `articles`.
   - Set up the Atlas Search feature to support vector searches. 

## Steps to Run:

### 1. **Run `main.py` for the First Time**:
When you first run `main.py`, it will execute the `setup_database()` function. This function will:
  - Load the AG News dataset.
  - Generate embeddings using **SentenceTransformer**.
  - Store the embeddings in **MongoDB**.
  - Create a vector index in MongoDB (you will manually create the index in Atlas later).

To run the script:
  ```bash
  python main.py
  ```

### 2. **Once the Setup is Complete**:
After the embeddings are generated and stored in MongoDB, and the vector index is created:
  - **Comment out** the `setup_database()` line in `main.py` (since the embeddings and index are already created).
  - Only keep the `perform_search()` function to perform subsequent searches without recreating the embeddings.

Example for subsequent searches:
  ```python
  # Uncomment this to perform searches without recreating the embeddings
  # setup_database()  # Comment this out after first run

  query = "Latest advancements in technology"
  perform_search(query)
  ```

### 3. **Steps to Create the Index Manually in MongoDB Atlas**:
Once you run `main.py` for the first time, you will see the vector index configuration printed out. You will need to manually create the vector index in MongoDB Atlas by following these steps:
  - Log in to **MongoDB Atlas** and navigate to your cluster.
  - Go to the **"Search"** tab under your database (you need to have the **Atlas Search** feature enabled, which may require a specific Atlas tier).
  - **Create a new index**:
    - Select your database (`ag_news_db`).
    - Choose the `articles` collection.
    - Click **Create Search Index** and choose the **custom index** option.
    - Paste the printed **vector index configuration** (shown below) into the index creation form in the Atlas UI.

Example vector index configuration:
  ```json
  {
    "fields": [
      {
        "numDimensions": 384,
        "path": "embedding",
        "similarity": "cosine",
        "type": "vector"
      }
    ]
  }
  ```

Save the index and wait for it to be built (it may take some time depending on the size of your data).

### 4. **Running the Code**:
After the vector index is created in MongoDB Atlas, you can run the script again. It will print the vector index configuration and show how to query the database using cosine similarity.

  ```bash
  python main.py
  ```

This will execute the `perform_search()` function and retrieve the most relevant articles based on the query.
