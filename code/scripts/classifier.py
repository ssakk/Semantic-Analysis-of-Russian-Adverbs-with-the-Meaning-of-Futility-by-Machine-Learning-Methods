from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from annotation import Corpus


first = Corpus('зря, напрасно', 'D:/subcorpus_test.txt')
example_corpus = first.annotation(aspect=True)
X = example_corpus['aspect']
# y = example_corpus['subject_embedding']
unique_elements, counts = np.unique(X, return_counts=True)
print(dict(zip(unique_elements, counts)))

# clf = RandomForestClassifier(n_estimators=100)
# clf.fit(X, y)
# feature_imp = pd.Series(clf.feature_importances_, index=['aacy', 'subject_emb']).sort_values(ascending=False)
#
# sns.barplot(x=feature_imp, y=feature_imp.index)
#
# plt.xlabel('Важность признаков')
# plt.ylabel('Признаки')
# plt.title('Визуализация важных признаков')
# plt.show()
