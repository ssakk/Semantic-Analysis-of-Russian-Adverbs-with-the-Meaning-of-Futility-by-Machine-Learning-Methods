from typing import List, Optional, Dict


class Word:
    """
    Class for parsing RuWAC token
    """

    def __init__(self, word: List[str]):
        self.word = word
        self.token, self.morphs, self.lemma, self.pos, self.x, self.y, self.sint = self.word

    def __str__(self):
        return self.lemma

    def word_class(self, word_classes: Dict[str, int]) -> int:
        if self.lemma in word_classes:
            return word_classes[self.lemma]
        else:
            raise ValueError('у слова нет класса')

    def animacy(self) -> Optional[str]:
        if self.pos == 'N':
            return self.morphs[5]
        elif self.pos == 'P':
            return None
        else:
            raise ValueError(f'wrong pos {self.pos}')

    def case(self) -> str:
        if self.pos == 'N':
            return self.morphs[4]
        elif self.pos == 'P':
            return self.morphs[5]
        else:
            raise ValueError(f'wrong pos {self.pos}')

    def person(self) -> Optional[str]:
        return self.morphs[4] if self.morphs[4] != '-' else None

    def tense(self) -> str:
        return self.morphs[3] if self.morphs[3] != '-' else None

    def aspect(self) -> str:
        return self.morphs[9] if self.morphs[9] != '-' else None
