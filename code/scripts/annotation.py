from typing import List, Dict, Any, Optional

import pandas as pd

from sentence import Sentence


class AnnotatedCorpus:
    def __init__(self, adverbs: str, corpus_path: str):
        self.adverbs = adverbs.split(', ')
        self.path = corpus_path
        self.corpus = pd.DataFrame(self.make_corpus())

    def make_corpus(self) -> Dict[str, List[Any]]:
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = content.split('\n\n\n')
            corpus = {'target_word': [], 'sentence': []}
            for s in sentences:
                tokens = [token.split('\t') for token in s.split('\n')]
                for i, token in enumerate(tokens):
                    for adverb in self.adverbs:
                        if token[2] == adverb:
                            corpus['target_word'].append(adverb)
                            sentence = Sentence(i, tokens)
                            corpus['sentence'].append(sentence)
        return corpus

    def annotation(self, subject_class: bool = False, animacy: bool = False, verb_class: bool = False,
                   person: bool = False, tense: bool = False, aspect: bool = False,
                   position: bool = False) -> pd.DataFrame:
        corpus_copy = self.corpus.copy(deep=True)
        corpus_copy['target'] = corpus_copy['target_word'].apply(lambda x: self.hash(x))
        if subject_class:
            corpus_copy['subject_class'] = corpus_copy['sentence'].apply(lambda x: x.get_subject_class())
        if animacy:
            corpus_copy['animacy'] = corpus_copy['sentence'].apply(lambda x: x.get_animacy())
        if verb_class:
            corpus_copy['verb_class'] = corpus_copy['sentence'].apply(lambda x: x.get_verb_class())
        if person:
            corpus_copy['person'] = corpus_copy['sentence'].apply(lambda x: x.get_person())
        if tense:
            corpus_copy['tense'] = corpus_copy['sentence'].apply(lambda x: x.get_tense())
        if aspect:
            corpus_copy['aspect'] = corpus_copy['sentence'].apply(lambda x: x.get_aspect())
        if position:
            corpus_copy['position'] = corpus_copy['sentence'].apply(lambda x: x.get_position())
        return corpus_copy

    @staticmethod
    def hash(word: str) -> Optional[int]:
        """
        Converts adverb to an integer representation using a given dictionary of hashes.

        Args:
            word: The adverb value.

        Returns:
            The integer representation of the word.
        """
        hash_table = {
            'напрасно': 0, 'зря': 1, 'тщетно': 2, 'безуспешно': 3, 'безрезультатно': 4, 'бесполезно': 5, 'впустую': 6,
            'понапрасну': 7, 'попусту': 8, 'всуе': 9, 'впусте': 10, 'вхолостую': 11, 'бездельно': 12, 'даром': 13
        }
        if word in hash_table:
            return hash_table[word]
        else:
            raise ValueError('является ли слово таргетом?')
