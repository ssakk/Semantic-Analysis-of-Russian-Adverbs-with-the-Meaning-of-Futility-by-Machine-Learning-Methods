from model import Model
model = Model()


class Word:
    def __init__(self, word):
        self.word = word.split('\t')
        self.token, self.morphs, self.lemma, self.pos, self.x, self.y, self.sint = self.word
        self.person = None
        self.embedding = None
        self.animacy = None
        self.tense = None
        self.aspect = None

    def __str__(self):
        return ' '.join(self.word)

    def get_embedding(self):
        if self.lemma in model:
            self.embedding = model(self.lemma)
        else:
            raise ValueError('Слова нет в модели')

    def get_animacy(self):
        pass

    def get_person(self):
        if self.pos == 'V':
            self.person = self.morphs.spilt()[0]


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tokens = sentence.split('\n')
        self.words = [Word(token) for token in self.tokens]

    def __str__(self):
        res = []
        for token in self.tokens:
            res.append(token.split('\t')[0])
        return ' '.join(res)

    def get_position(self):
        pass

    def get_annotation(self):
        pass


with open('D:/subcorpus_1.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    sentences = content.split('\n\n\n')

x = Sentence(sentences[0])
y = Word('беспокоили	Vmis-p-a-e	беспокоить	V	29	26	подч-союзн')
print(y.lemma)
