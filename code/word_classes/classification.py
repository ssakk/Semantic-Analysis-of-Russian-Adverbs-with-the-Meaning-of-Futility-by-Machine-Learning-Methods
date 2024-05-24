from typing import List, Tuple
import csv

import gensim
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

from code.word_classes.model import Model


class Clustering:
    def __init__(self, doc_path: str, norm: bool = False):
        self.path = doc_path
        print('Начало загрузки модели')
        self.model = Model().model
        print('Конец загрузки модели')
        self.words = self.read()
        self.vectors = np.array([self.embedding(word, self.model) for word in self.words])
        if norm:
            print('Произвожу нормализацию')
            self.vectors = self.normilize(self.vectors)

    def read(self) -> List[str]:
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            words = list(reader)[0]
        return words

    @staticmethod
    def embedding(word, vector_model: gensim.models.fasttext.FastTextKeyedVectors) -> np.ndarray:
        if word in vector_model:
            emb = vector_model[word]
        else:
            emb = np.ndarray(0)
            print(f'Слова {word} нет в модели')
        return emb

    @staticmethod
    def normilize(vectors: np.ndarray) -> np.ndarray:
        scaler = MinMaxScaler()
        return scaler.fit_transform(vectors)

    def best_cluster_number(self, word: str, viz: bool = True) -> Tuple[int, List[int]]:
        silhouette_scores = []
        for i in range(10, 101):
            print(i)
            preds = self.perform_cluster(n_clusters=i)
            silhouette = silhouette_score(self.vectors, preds)
            silhouette_scores.append(silhouette)
        if viz:
            plt.figure(figsize=(10, 4))
            plt.scatter(x=[i for i in range(10, 101)], y=silhouette_scores, s=70, c='#a689c9')
            plt.grid(True)
            plt.xlabel("Количество кластеров", fontsize=15)
            plt.ylabel("Коэффициент силуэта", fontsize=15)
            plt.xticks(range(10, 101, 10), fontsize=15)
            plt.yticks(fontsize=15)
            plt.savefig(f'{word}.png')
            plt.show()
        return silhouette_scores.index(max(silhouette_scores)) + 10, silhouette_scores

    def perform_cluster(self, n_clusters: int) -> np.ndarray:
        clst = AgglomerativeClustering(n_clusters=n_clusters)
        preds = clst.fit_predict(self.vectors)
        return preds


path_subjects = '../subcorpus/all_subjects.csv'
path_verbs = '../subcorpus/all_verbs.csv'
xu, z = Clustering(path_subjects, norm=True).best_cluster_number('subj_with_norm')
print(xu, z)
