from typing import List, Dict, Any, Optional
import pandas as pd
from collections import defaultdict
from code.scripts.sentence import Sentence


class AnnotatedCorpus:
    """
    Represents an annotated corpus of sentences containing target words (adverbs).

    Attributes:
        adverbs (List[str]): The list of target adverbs.
        path (str): The file path of the corpus.
        corpus (pd.DataFrame): The raw corpus data.
        annotated_corpus (pd.DataFrame): The annotated corpus data.
        hash_table (Dict[str, int]): A dictionary that maps target adverbs to their hash values.

    Methods:
        create_hash_table() -> Dict[str, int]:
            Creates a hash table for the target adverbs.
        load_corpus() -> Dict[str, List[Any]]:
            Constructs the raw corpus data from the file.
        annotate_corpus() -> pd.DataFrame:
            Annotates the corpus data with various linguistic features.
        get_hash(word: str) -> Optional[int]:
            Hashes the target adverbs and returns the corresponding integer value.
    """

    def __init__(self, adverbs: str, corpus_path: str):
        """
        Initializes the AnnotatedCorpus instance.

        Args:
            adverbs (str): A comma-separated string of target adverbs.
            corpus_path (str): The file path of the corpus.
        """
        self.adverbs = adverbs.split(', ')
        self.path = corpus_path
        self.hash_table = self.create_hash_table()
        self.corpus = pd.DataFrame(self.load_corpus())
        self.annotated_corpus = self.annotate_corpus()

    def create_hash_table(self) -> Dict[str, int]:
        """Creates a hash table for the target adverbs."""
        return {adverb: idx for idx, adverb in enumerate(set(self.adverbs))}

    def load_corpus(self) -> Dict[str, List[Any]]:
        """Constructs the raw corpus data from the file."""
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            sentences = content.split('\n\n\n')
            corpus = {'target_word': [], 'sentence': []}
            for s in sentences:
                tokens = [token.split('\t') for token in s.split('\n')]
                for i, token in enumerate(tokens):
                    adverb = token[2]
                    if adverb in self.adverbs:
                        corpus['target_word'].append(adverb)
                        sentence = Sentence(i, tokens)
                        corpus['sentence'].append(sentence)
        return corpus

    def annotate_corpus(self) -> pd.DataFrame:
        """Annotates the corpus data with various linguistic features."""
        corpus_copy = self.corpus.copy(deep=True)
        corpus_copy['target'] = corpus_copy['target_word'].apply(self.get_hash)
        corpus_copy['subject_class'] = corpus_copy['sentence'].apply(lambda x: x.get_subject_class())
        corpus_copy['animacy'] = corpus_copy['sentence'].apply(lambda x: x.get_animacy())
        corpus_copy['subject_pos'] = corpus_copy['sentence'].apply(lambda x: x.get_subject_pos())
        corpus_copy['verb_negation'] = corpus_copy['sentence'].apply(lambda x: x.get_verb_negation())
        corpus_copy['verb_class'] = corpus_copy['sentence'].apply(lambda x: x.get_verb_class())
        corpus_copy['person'] = corpus_copy['sentence'].apply(lambda x: x.get_person())
        corpus_copy['tense'] = corpus_copy['sentence'].apply(lambda x: x.get_tense())
        corpus_copy['aspect'] = corpus_copy['sentence'].apply(lambda x: x.get_aspect())
        corpus_copy['adverb_negation'] = corpus_copy['sentence'].apply(lambda x: x.get_adverb_negation())
        corpus_copy['position'] = corpus_copy['sentence'].apply(lambda x: x.get_position())
        return corpus_copy

    def get_hash(self, word: str) -> Optional[int]:
        """
        Hashes the target adverbs into an integer value.

        Args:
            word (str): The target adverb.
        
        Returns:
            Optional[int]: Hash value or None if not found.
        """
        if word in self.hash_table:
            return self.hash_table[word]
        raise ValueError(f'The word "{word}" is not a target adverb.')
