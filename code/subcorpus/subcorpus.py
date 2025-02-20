from typing import List, Dict, Tuple
import csv
from code.scripts.sentence import Sentence

all_adverbs = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, ' \
              'всуе, впусте, вхолостую, бездельно, даром'


class Subcorpus:
    def __init__(self, adverbs: str, corpus_path: str):
        self.adverbs = set(adverbs.split(', '))
        self.path = corpus_path
        self.sentences = self.read()

    def read(self) -> List[str]:
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                content = file.read()
                return content.split('\n\n\n')
        except FileNotFoundError:
            print(f"Error: The file {self.path} was not found.")
            return []

    def count_stats(self, name1: str = 'freq_stats.txt', name2: str = 'predic_stats.txt', write: bool = True) -> \
            Tuple[Dict[str, int], Dict[str, int]]:
        freq_stats = {adverb: 0 for adverb in self.adverbs}
        predic_stats = {adverb: 0 for adverb in self.adverbs}

        for s in self.sentences:
            tokens = [token.split('\t') for token in s.split('\n')]
            for token in tokens:
                if token[2] in self.adverbs:
                    freq_stats[token[2]] += 1
                    if token[6] != 'обст':
                        predic_stats[token[2]] += 1

        if write:
            with open(name1, 'a', encoding='utf-8') as file1:
                for k, v in freq_stats.items():
                    file1.write(f"{k}\t{v}\n")

            with open(name2, 'a', encoding='utf-8') as file2:
                for k, v in predic_stats.items():
                    file2.write(f"{k}\t{v}\n")

        return freq_stats, predic_stats

    def subjects_and_verbs(self, name1: str = 'all_subjects.csv', name2: str = 'all_verbs.csv', write: bool = True) -> \
            Tuple[List[str], List[str]]:
        subjects = []
        verbs = []

        for s in self.sentences:
            tokens = [token.split('\t') for token in s.split('\n')]
            for i, token in enumerate(tokens):
                if token[2] in self.adverbs:
                    sentence = Sentence(i, tokens)
                    verb = str(sentence.get_verb())
                    if verb and verb not in verbs:
                        verbs.append(verb)
                    subject = str(sentence.get_subject())
                    if subject and subject not in subjects:
                        subjects.append(subject)

        if write:
            with open(name1, 'a', encoding='utf-8') as file1:
                writer = csv.writer(file1)
                writer.writerow(subjects)

            with open(name2, 'a', encoding='utf-8') as file2:
                writer = csv.writer(file2)
                writer.writerow(verbs)

        return subjects, verbs


subcorpus = Subcorpus(all_adverbs, 'D:/subcorpus1.txt')
subcorpus.count_stats()
subcorpus.subjects_and_verbs()
