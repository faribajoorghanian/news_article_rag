

from datasets import load_dataset

def load_ag_news():
    """
    Load the AG News dataset from Hugging Face Datasets.
    Returns the dataset object.
    """
    dataset = load_dataset("ag_news")
    
    return dataset

def preprocess_data(dataset):
    """
    Preprocess the AG News dataset and extract article texts.
    Args:
    - dataset: AG News dataset object
    
    Returns:
    - texts: List of text articles from the 'train' split
    """
    texts = [article["text"] for article in dataset["train"]]  # Use the "train" split for learning
    return texts

