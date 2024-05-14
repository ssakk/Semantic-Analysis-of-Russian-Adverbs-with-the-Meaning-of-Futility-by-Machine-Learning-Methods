from description import Word, Sentence
from typing import List, Dict, Any
import pandas as pd


class Corpus:
    def __init__(self, adverbs: str, corpus_path: str):
        self.adverbs = adverbs.split(', ')
        self.path = corpus_path
        self.corpus = pd.DataFrame(self.make_corpus())

    def make_corpus(self) -> Dict[str, List[Any]]:
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = content.split('\n\n\n')
            corpus = {'target_word': [], 'text': [], 'sentence': []}
            for s in sentences:
                tokens = [token.split('\t') for token in s.split('\n')]
                for i, token in enumerate(tokens):
                    for adverb in self.adverbs:
                        if token[2] == adverb:
                            corpus['target_word'].append(adverb)
                            sentence = Sentence(i, tokens)
                            corpus['text'].append(str(sentence))
                            corpus['sentence'].append(sentence)
        return corpus

    def annotation(self, verb_embedding: bool = False, subject_embedding: bool = False,
                   position: bool = False) -> pd.DataFrame:
        corpus_copy = self.corpus.copy(deep=True)
        if verb_embedding:
            corpus_copy['verb_embedding'] = corpus_copy['sentence'].apply(lambda x: x.get_verb_embedding())
        if subject_embedding:
            corpus_copy['subject_embedding'] = corpus_copy['sentence'].apply(lambda x: x.get_subject_embedding())
        if position:
            corpus_copy['subject_embedding'] = corpus_copy['sentence'].apply(lambda x: x.get_position())

        return corpus_copy


first = Corpus('бесполезно', 'D:/subcorpus_1.txt')
example_corpus = first.corpus
# y = Word('беспокоили	Vmis-p-a-e	беспокоить	V	29	26	подч-союзн')
print(example_corpus)
