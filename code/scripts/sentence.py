from typing import List, Optional

import numpy as np

from word import Word
from model import Model
model = Model().model


class Sentence:
    """
    Class for parsing RuWAC sentences
    """

    def __init__(self, index: int, sentence: List[List[str]]):
        self.index = index
        self.tokens = sentence
        self.adverb = Word(self.tokens[self.index])
        self.verb = self.get_verb()
        self.subject = self.get_subject() if self.verb else None

    def get_verb(self) -> Optional[Word]:
        if self.adverb.sint == 'обст':
            prob_verb = Word(self.tokens[int(self.adverb.y) - 1])
            verb = prob_verb if prob_verb.pos == 'V' else None
        else:
            verb = None
        return verb

    def get_subject(self) -> Optional[Word]:
        subjects = []
        for token in self.tokens:
            word = Word(token)
            if word.y == self.verb.x and word.sint == 'предик' and (word.pos == 'N' or word.pos == 'P'):
                if word.case() == 'n':
                    subjects.append(word)
        if len(subjects) == 0:
            subject = None
        elif len(subjects) == 1:
            subject = subjects[0]
        else:
            nouns = [subject for subject in subjects if subject.pos == 'N']
            if len(nouns) == 0:
                subject = self.get_closest_word(self.index, subjects)
            else:
                subject = self.get_closest_word(self.index, nouns)
        return subject

    def __str__(self):
        res = []
        for token in self.tokens:
            res.append(token[0])
        return ' '.join(res)

    @staticmethod
    def get_closest_word(position: int, words: List[Word]) -> Word:
        closest_word = None
        min_distance = float('inf')

        for word in words:
            distance = abs(position - int(word.x))
            if distance < min_distance:
                closest_word = word
                min_distance = distance

        return closest_word

    def get_subject_embedding(self) -> Optional[np.ndarray]:
        if self.subject:
            return self.subject.embedding(model)
        else:
            return None

    def get_animacy(self) -> Optional[int]:
        if self.subject:
            if self.subject.animacy() == 'n':
                return 0
            elif self.subject.animacy() == 'y':
                return 1
            else:
                return None
        else:
            return None

    def get_verb_embedding(self) -> Optional[np.ndarray]:
        if self.verb:
            return self.verb.embedding(model)
        else:
            return None

    def get_person(self) -> Optional[int]:
        if self.verb:
            if self.verb.person():
                return int(self.verb.person())
            else:
                return 0
        else:
            return None

    def get_tense(self) -> Optional[int]:
        if self.verb:
            if self.verb.tense() == 'p':
                return 2
            elif self.verb.tense() == 'f':
                return 3
            elif self.verb.tense() == 's':
                return 1
            else:
                return 0
        else:
            return None

    def get_aspect(self) -> Optional[int]:
        if self.verb:
            if self.verb.aspect() == 'p':
                return 3
            elif self.verb.aspect() == 'e':
                return 1
            elif self.verb.aspect() == 'b':
                return 2
            else:
                return 0
        else:
            return None

    def get_position(self) -> Optional[int]:
        if self.verb:
            if self.adverb.x > self.verb.x:
                return 0
            else:
                return 1
        else:
            return None
