# Subcorpus Analysis

## Description
This directory contains the code with analyzing the subcorpus of Russian adverbs related to the meaning of futility. The scripts here are designed to preprocess the data, extract relevant features

## Files
- [collecting.py](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/collecting.py) — the script processes RUWAC to extract sentences containing specific lexemes related to futility;
- [subcorpus.py](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/subcorpus.py) — the script processes collected text corpus to analyze the usage of specified adverbs related to futility. It counts the frequency of each adverb, and identifies the subjects and verbs associated with those adverbs;
- [all_subjects.csv](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/all_subjects.csv), [all_verbs.csv](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/all_verbs.csv) — files with collected subjects and verbs;
- [freq_stats.txt](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/freq_stats.txt), [predic_stats.txt](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/subcorpus/predic_stats.txt) — files containing frequency statistics and predicate usage statistics.
