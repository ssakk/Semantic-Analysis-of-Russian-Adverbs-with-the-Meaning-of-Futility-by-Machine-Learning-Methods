with open('D:/subcorpus.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    sentences = content.split('\n\n\n')

sentences_per_file = len(sentences) // 10

for i in range(10):
    start = i * sentences_per_file
    end = (i + 1) * sentences_per_file if i < 9 else len(sentences)
    with open(f'subcorpus_{i+1}.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(sentences[start:end]))
