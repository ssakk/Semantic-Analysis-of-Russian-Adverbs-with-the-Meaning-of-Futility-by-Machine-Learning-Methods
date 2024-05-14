from typing import List
from model import Model
model = Model().model


class Word:
    def __init__(self, word: List[str]):
        self.word = word
        self.token, self.morphs, self.lemma, self.pos, self.x, self.y, self.sint = self.word
        self.embedding = None
        if self.pos == 'N':
            self.person = None
            self.animacy = None
        elif self.pos == 'P':
            self.person = None
            self.animacy = 1
        elif self.pos == 'V':
            self.tense = None
            self.aspect = None
        else:
            pass

    def __str__(self):
        return ' '.join(self.word)

    def get_embedding(self):
        print(self.lemma, self.pos)
        if self.lemma + self.pos in model:
            self.embedding = model(self.lemma)
        else:
            self.embedding = None
            raise ValueError('Слова нет в модели')
        return self.embedding

    def get_animacy(self):
        pass

    def get_person(self):
        if self.pos == 'V':
            self.person = self.morphs.spilt()[0]


class Sentence:
    def __init__(self, position: int, sentence: List[List[str]]):
        self.tokens = sentence
        self.adverb = Word(self.tokens[position])

    def __str__(self):
        res = []
        for token in self.tokens:
            res.append(token[0])
        return ' '.join(res)

    def get_position(self) -> int:
        pass

    def get_verb_embedding(self) -> int:
        pass

    def get_subject_embedding(self) -> int:
        pass
