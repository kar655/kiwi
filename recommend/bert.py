import os

import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Bert:
    def __init__(self):
        if 'bert-model' in os.listdir():
            self.model = SentenceTransformer('./bert-model')
        else:
            self.model = SentenceTransformer('bert-base-nli-mean-tokens')
            self.model.save('bert-model')

        self.model.eval()

    def encode(self, data: List[str]):
        return self.model.encode(data)

    def top_predictions(self, sentence: str, embedded, n: int = 20):
        encoded = self.model.encode([sentence])
        predictions = np.array(
            sorted(enumerate(embedded), key=lambda x: cosine_similarity([x[1]], encoded), reverse=True))

        # ???
        scores = [cosine_similarity([embedding], encoded).tolist()[0][0] for embedding in predictions[:n, 1]]
        print(scores)

        return np.array(predictions[:n, 0], dtype=int)
