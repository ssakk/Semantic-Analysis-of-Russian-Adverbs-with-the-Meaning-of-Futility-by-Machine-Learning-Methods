from tqdm import tqdm


lexemes = 'напрасно, зря, тщетно, безуспешно, безрезультатно, бесполезно, впустую, понапрасну, попусту, ' \
          'даром, впусте, втуне, всуе, вхолостую, бездельно'
target = set(lexeme.strip() for lexeme in lexemes.split(', '))

current_sentence = ''

with open('subcorpus.txt', 'a', encoding='utf-8') as output_file:
    with open('ruwac-filtered.out', encoding='utf-8') as f:
        for line in tqdm(f, desc='Processing', unit=' lines'):
            if line.startswith('<'):
                continue
            elif 'SENT' in line:
                if any(lexeme in current_sentence for lexeme in target):
                    output_file.write(current_sentence + '\n\n')
                current_sentence = ''
            else:
                current_sentence += line
