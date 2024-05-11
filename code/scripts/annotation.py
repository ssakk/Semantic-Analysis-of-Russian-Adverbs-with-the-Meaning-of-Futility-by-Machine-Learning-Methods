from description import Word, Sentence
from typing import List, Dict, Any


class Corpus:
    def __init__(self, adverbs: str, corpus_path: str):
        self.adverbs = adverbs.split(', ')
        self.path = corpus_path
        self.corpus = self.make_corpus()

    def make_corpus(self) -> Dict[str, List[Any]]:
        with open(self.path, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = content.split('\n\n\n')
            corpus = {'target_word': [], 'text': [], 'sentence': []}
            for s in sentences:
                tokens = [token.split('\t') for token in s.split('\n')]
                for token in tokens:
                    for adverb in self.adverbs:
                        if token[2] == adverb:
                            corpus['target_word'].append(adverb)
                            corpus['text'].append(str(Sentence(tokens)))
                            corpus['sentence'].append(Sentence(tokens))
        return corpus


first = Corpus('бесполезно', 'D:/subcorpus_1.txt')
corpus = first.corpus
# y = Word('беспокоили	Vmis-p-a-e	беспокоить	V	29	26	подч-союзн')
print(corpus['sentence'][0].words[0])
