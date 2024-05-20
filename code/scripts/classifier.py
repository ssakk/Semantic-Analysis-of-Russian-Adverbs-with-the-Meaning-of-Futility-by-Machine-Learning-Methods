from typing import List, Sequence

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=100)

from annotation import AnnotatedCorpus


class Experiment:
    def __init__(self, target_adverbs: str, corpus_path: str, parameters: List[Sequence]):
        self.adverbs = target_adverbs
        self.path = corpus_path
        self.parameters = parameters
        self.corpus = AnnotatedCorpus(self.adverbs, self.path).annotation(*parameters)

    def classification(self, clf):
        X = self.corpus[self.parameters]
        y = self.corpus['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)


        feature_imp = pd.Series(clf.feature_importances_, index=self.parameters).sort_values(ascending=False)
        sns.barplot(x=feature_imp, y=feature_imp.index)
        plt.xlabel('Важность признаков')
        plt.ylabel('Признаки')
        plt.title('Визуализация важных признаков')
        plt.show()

