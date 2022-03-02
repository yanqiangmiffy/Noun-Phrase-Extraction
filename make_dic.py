import pandas as pd

train = pd.read_table('data/train/span_extract_train.txt', sep='\t')
print(train)

with open('data/dic.txt', 'w', encoding='utf-8') as f:
    for word in train['名词短语']:
        # print(word.split('_|_'))
        for nw in word.split('_|_'):
            nw=''.join(nw.split())
            if len(nw)>=2:
                f.write(f'{nw} 1000 n\n')
