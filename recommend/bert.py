import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Bert:
    def __init__(self):
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')
        print("Bert is loaded")

    def encode(self, data: List[str]):
        return self.model.encode(data)

    def top_predictions(self, sentence: str, embedded, n: int = 20):
        encoded = self.model.encode([sentence])
        predictions = np.array(
            sorted(enumerate(embedded), key=lambda x: cosine_similarity([x[1]], encoded), reverse=True))
        return np.array(predictions[:n, 0], dtype=int)
