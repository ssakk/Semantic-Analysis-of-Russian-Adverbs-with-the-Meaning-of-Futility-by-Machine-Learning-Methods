adverbs = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, ' \
        'всуе, впусте, вхолостую, бездельно, даром'
list_adverbs = adverbs.split(', ')

current_sentence = ''
target_adverbs = ['\t' + adverb for adverb in list_adverbs]
with open('lines_3000000.txt',  encoding='utf-8') as f:
    for line in f:
        if 'SENT' in line:
            current_sentence += '\n\n'
            if any(verb in current_sentence for verb in target_adverbs):
                with open('subcorpus.txt', 'a', encoding='utf-8') as file:
                    file.write(current_sentence)
            current_sentence = ''
        else:
            current_sentence += line
