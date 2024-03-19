with open('D:/subcorpus.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    sentences = content.split('\n\n\n')
    print(sentences[0])
