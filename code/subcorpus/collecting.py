from tqdm import tqdm


lexemes = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, ' \
          'даром, впусте, втуне, всуе, вхолостую, бездельно'
target = ['\t' + lexeme for lexeme in lexemes.split(', ')]
current_sentence = ''

with open('ruwac-filtered.out', encoding='utf-8') as f:
    for line in tqdm(f, desc='Processing', unit=' lines'):
        if line.startswith('<'):
            pass
        elif 'SENT' in line:
            current_sentence += '\n\n'
            if any(lexeme in current_sentence for lexeme in target):
                with open('subcorpus.txt', 'a', encoding='utf-8') as file:
                    file.write(current_sentence)
            current_sentence = ''
        else:
            current_sentence += line
