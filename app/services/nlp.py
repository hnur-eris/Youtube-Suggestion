import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from transformers import BertTokenizer, BertModel
import torch
from typing import List, Tuple


class TextProcessor:
    def __init__(self, n_clusters: int = 20):
        self.n_clusters = n_clusters
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.kmeans = KMeans(n_clusters=n_clusters)
        self.bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.bert_model = BertModel.from_pretrained('bert-base-uncased')
        
    def process_text(self, text: str) -> np.ndarray:
        """Process text using BERT and return vector representation"""
        inputs = self.bert_tokenizer(text, return_tensors="pt", 
                                   truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).numpy()
    
    def fit_clusters(self, texts: List[str]) -> None:
        """Fit the clustering model on the given texts"""
        vectors = np.vstack([self.process_text(text) for text in texts])
        self.kmeans.fit(vectors)
    
    def predict_cluster(self, text: str) -> int:
        """Predict the cluster for a given text"""
        vector = self.process_text(text)
        return self.kmeans.predict(vector)[0]
    
    def get_similar_videos(self, video_id: int, n_recommendations: int = 5) -> List[int]:
        """Get similar videos based on cluster membership"""
        # This would be implemented based on your database structure
        pass 