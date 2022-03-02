import pandas as pd

train = pd.read_csv('data/train/span_extract_train.txt', sep='\t')

texts = []

tags = []

for index, row in train.iterrows():
    text = row['用户问句']
    text = ''.join(text.split())
    texts.append([w for w in text])
    print([w for w in text])

    tag = ['O'] * len(text)
    print(tag)

    words = row['名词短语']
    words = ''.join(words.split())

    print([w for w in words.split('_|_')])

    for noun in words.split('_|_'):
        start_index = text.index(noun)
        print(text[start_index:start_index + len(noun)])
        for i in range(start_index, start_index + len(noun)):
            if i == start_index:
                tag[i] = 'B-NOUN'
            else:
                tag[i] = 'I-NOUN'
    print(tag)
    print("====" * 10)
    tags.append(tag)

with open('data/train.txt', 'w', encoding='utf-8') as f:
    for text, tag in zip(texts, tags):
        # text = '\n'.join(text)
        # tag = '\n'.join(tag)
        # f.write(f'{text} {tag}')
        for c, t in zip(text, tag):
            f.write(f'{c} {t}\n')
        f.write('\n')
