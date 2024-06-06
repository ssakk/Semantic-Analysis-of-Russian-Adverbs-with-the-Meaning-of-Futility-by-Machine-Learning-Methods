from typing import List
import csv
import json

import gensim
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

from code.word_classes.model import Model
purple = '#a689c9'


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

    def best_cluster_number(self, name: str, viz: bool = True) -> int:
        silhouette_scores = []
        for i in range(10, 201):
            print(i)
            preds = self.perform_cluster(n_clusters=i)
            silhouette = silhouette_score(self.vectors, preds)
            silhouette_scores.append(silhouette)
        if viz:
            plt.figure(figsize=(10, 4))
            plt.scatter(x=[i for i in range(10, 201)], y=silhouette_scores, s=50, c=purple)
            plt.grid(True)
            plt.xlabel("Количество кластеров", fontsize=15)
            plt.ylabel("Коэффициент силуэта", fontsize=15)
            plt.xticks(range(10, 201, 10), fontsize=15)
            plt.yticks(fontsize=15)
            plt.savefig(f'{name}.png')
            plt.show()
        return silhouette_scores.index(max(silhouette_scores)) + 10

    def perform_cluster(self, n_clusters: int, final: bool = False, name: str = None) -> np.ndarray:
        clst = AgglomerativeClustering(n_clusters=n_clusters)
        preds = clst.fit_predict(self.vectors)

        if final:
            res = {}
            for word, word_class in zip(self.words, preds):
                res[word] = str(word_class)
            with open(f'{name}.json', 'w', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False)

        return preds


path_subjects = '../subcorpus/all_subjects.csv'
path_verbs = '../subcorpus/all_verbs.csv'

S = Clustering(path_subjects)
V = Clustering(path_verbs)

num_subject_clusters = S.best_cluster_number('subj_num_clusters')
print(num_subject_clusters)
num_verb_clusters = V.best_cluster_number('verb_withot_norm')
print(num_subject_clusters, num_verb_clusters)

pred_subjects = S.perform_cluster(num_subject_clusters, final=True, name='subjects_classes')
pred_verbs = V.perform_cluster(num_verb_clusters, final=True, name='verbs_classes')
