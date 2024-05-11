adverbs = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, ' \
        'всуе, впусте, вхолостую, бездельно, даром'
list_adverbs = adverbs.split(', ')

with open('D:/subcorpus1.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    sentences = content.split('\n\n\n')
count_tokens = 0
verb_stats = {}
for verb in list_adverbs:
    verb_stats[verb] = 0

for s in sentences:
    tokens = [token.split('\t') for token in s.split('\n')]
    count_tokens += len(tokens)
    for line in tokens:

        if any(verb in line for verb in list_adverbs):
            target_line = line
            target_verb = target_line[0].lower()
            if target_verb in ['зри', 'зрях', 'всуй', 'дароме', 'дарома']:
                pass
            else:

                verb_stats[target_verb] += 1

with open('verb_stats.txt', 'a', encoding='utf-8') as s:
    for k in verb_stats:
        s.write(k+'\t'+str(verb_stats[k])+'\n')
