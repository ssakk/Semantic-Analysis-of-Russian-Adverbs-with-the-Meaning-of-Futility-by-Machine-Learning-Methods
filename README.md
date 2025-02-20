# Semantic Analysis of Russian Adverbs with the Meaning of Futility by Machine Learning Methods

## Abstract
This study explores the semantics and contextual usage of adverbs with the meaning of futility in Russian discourse using machine learning (ML) methods, specifically classification. The research aims to provide a comprehensive analysis of the structure of the aforementioned semantic field, as well as to identify the contextual distribution of the lexical units in question. Through the collection and markup of relevant texts, the study will train classifiers to find correlations among marking parameters and lexical units. The findings are expected to contribute to a more accurate understanding of the semantic field and shed light on the principles governing the interaction between various factors influencing the selection of appropriate synonyms.

## Technologies
- Python
- scikit-learn
- pandas
- numpy

## Collected data and statistics
| Adverb | Occurrences | Predicate Occurrences | Share of Predicate Occurrences (%) |
|--------------------------|-------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------|
| naprasno                 | 19543                               | 8076                                                     | 41.3                                                                |
| zrya                     | 65040                               | 16351                                                    | 25.1                                                                |
| tshchetno                | 8240                                | 2634                                                     | 32.0                                                                |
| bezuspesno               | 9201                                | 3728                                                     | 40.5                                                                |
| bezrezul'tatno          | 4519                                | 2711                                                     | 60.0                                                                |
| vpustuyu                 | 5770                                | 1016                                                     | 17.6                                                                |
| ponaprasnu               | 2114                                | 354                                                      | 16.7                                                                |
| popustu                  | 2491                                | 370                                                      | 14.9                                                                |
| darom                    | 19489                               | 5522                                                     | 28.3                                                                |

## Annotation
The annotation process was fully automated, with the main annotation code implemented in the script [annotation.py](https://github.com/ssakk/Semantic-Analysis-of-Russian-Adverbs-with-the-Meaning-of-Futility-by-Machine-Learning-Methods/blob/main/code/scripts/annotation.py). The final list of annotation parameters for sentences in the corpus is as follows:

- Target Adverb
- Presence of Negation with the Adverb
- Subject Class made up from a distributional semantic embedding from a pretrained language model
- Subject Animacy
- Subject Part of Speech
- Presence of Negation with the Verb
- Verb Class made up from a distributional semantic embedding from a pretrained language model
- Verb Person
- Verb Tense
- Verb Aspect
- Word Order of Adverb, Verb, and Subject

## Experiments
This section presents the results of five experiments assessing the importance of features when training the Random Forest Classifier (RFC) model on various groups of adverbs.
### Experiment 1
The first experiment was conducted on all adverbs.
![Experiment1](plots/plot1.png)
### Experiment 2
The second one was running on *zrya*, *naprasno*, and *tshchetno*.
![Experiment2](plots/plot2.png)
### Experiment 3
The third experiment was conducted on the adverbs *tshchetno*, *bezuspeshno*, *bezrezul'tatno*, and *bespolezno*.
![Experiment3](plots/plot3.png)
### Experiment 4
The fourth experiment was conducted separately on the adverbs *tshchetno* and *bespolezno* within balanced classes to test the hypothesis of retrospective temporal opposition of these adverbs in the literature on the topic.
![Experiment4](plots/plot4.png)
### Experiment 5
In the final experiment, the adverbs vputyu, ponaprasnu, popustu, and darom will be examined.
![Experiment5](plots/plot5.png)

## Results
- The most important contextual property for adverb selection is the semantic class of the controlling verb.
- Other significant parameters for different adverb groups include noun class, word order in the sentence, and the presence of negation with the adverb.
- All other selected features have a considerably lesser impact on synonym selection.
- Factors such as person, tense, and aspect of the controlling verb, previously deemed relevant in literature based on manual context selection and non-computer analysis, did not prove significant in this study.
