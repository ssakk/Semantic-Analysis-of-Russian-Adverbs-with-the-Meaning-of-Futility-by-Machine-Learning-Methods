from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from imblearn.under_sampling import RandomUnderSampler

from code.scripts.annotation import AnnotatedCorpus
purple = '#a689c9'
blue = '#cdddf0'


class Experiment:
    def __init__(self, target_adverbs: str, corpus: pd.DataFrame, balanced: bool = False):
        self.adverbs = target_adverbs
        self.parameters = ['subject_class', 'animacy', 'subject_pos', 'verb_negation', 'verb_class', 'person', 'tense',
                           'aspect', 'adverb_negation', 'position']
        self.corpus = corpus.dropna()
        self.balanced = balanced

    def random_forest(self, num, param_grid):
        X = self.corpus[self.parameters]
        y = self.corpus['target']
        if self.balanced:
            rus = RandomUnderSampler()
            X, y = rus.fit_resample(X, y)
        most_frequent_label = y.mode()[0]
        y_pred_baseline = [most_frequent_label] * len(y)
        baseline = accuracy_score(y, y_pred_baseline)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
        search_clf = GridSearchCV(RandomForestClassifier(), param_grid=param_grid, cv=5)
        search_clf.fit(X_train, y_train)
        best_params = search_clf.best_params_
        clf = RandomForestClassifier(**best_params)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        test_score = accuracy_score(y_test, y_pred)

        print(test_score, baseline)
        if test_score > baseline:
            feature_imp = pd.Series(clf.feature_importances_, index=self.parameters).sort_values(ascending=False)
            print(type(feature_imp))
            sns.barplot(x=feature_imp, y=feature_imp.index, color=blue)
            plt.xlabel('Важность признаков')
            plt.ylabel('Признаки')
            plt.savefig(f'feature_importance{num}.png')
            plt.show()

    def decision_tree(self, features: List[str], adverbs: str):
        X = self.corpus[features]
        y = self.corpus['target']
        if self.balanced:
            rus = RandomUnderSampler()
            X, y = rus.fit_resample(X, y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
        clf = DecisionTreeClassifier(max_depth=3, random_state=42)
        clf = clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        test_score = accuracy_score(y_test, y_pred)
        print(test_score)

        fig = plt.figure(figsize=(20, 15))
        _ = plot_tree(clf, feature_names=features, class_names=adverbs.split(','))
        fig.savefig("decistion_tree1.png")


grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['gini', 'entropy'],
    'max_features': ['sqrt', 'log2', None],
    'max_depth': [10, 100, 1000],
    'n_jobs': [-1]
}
adverb1 = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, даром'
adverb2 = 'напрасно, зря, тщетно'
adverb3 = 'тщетно, безуспешно, безрезультатно, бесполезно'
adverb4 = 'тщетно, бесполезно'
adverb5 = 'впустую, понапрасну, попусту, даром'

feature1 = ['subject_class', 'adverb_negation', 'position']
feature3 = ['verb_class', 'subject_class', 'position', 'animacy']
feature4 = ['verb_class', 'subject_class', 'position', 'aspect', 'tense']
feature5 = ['subject_class']

corpusa = AnnotatedCorpus(adverb1, 'D:/subcorpus1.txt').annotated_corpus
x = Experiment(adverb1, corpusa, balanced=True)
# x.random_forest(1, grid)
x.decision_tree(feature5, adverb1)
