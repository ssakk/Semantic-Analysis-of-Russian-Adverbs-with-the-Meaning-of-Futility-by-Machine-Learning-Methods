import json

# Загрузка данных из файла
with open('verbs_classes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание словаря для хранения слов по классам
classes = {}

# Разделение строк и сохранение слов по классам
for word, class_num in data.items():
    if class_num not in classes:
        classes[class_num] = []
    classes[class_num].append(word)

res = []
# Вывод результата
for class_num, words in classes.items():
    one_class = {
        'class_number': class_num,
        'class_length': len(words),
        'words': words}
    res.append(one_class)

with open(f'verbs.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=4)
