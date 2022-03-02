import jieba
import jieba.analyse
import jieba.posseg
import jieba.posseg as psg
import pandas as pd


jieba.set_dictionary('data/dic.txt')
test = pd.read_table('data/test_a/span_extrace_test_A.txt', sep='\t')


def dosegment_all(sentence):
    '''
    带词性标注，对句子进行分词，不排除停词等
    :param sentence:输入字符
    :return:
    '''
    sentence_seged = jieba.posseg.cut(sentence.strip())
    outstr = ''
    for x in sentence_seged:
        if x.flag.startswith('n'):
            outstr += "{}_|_".format(x.word)
    # outstr = ",".join([("%s/%s" %(x.word,x.flag)) for x in sentence_seged])
    outstr = outstr.rstrip('_|_')
    return outstr


test['名词短语'] = test['用户问句'].apply(lambda x: dosegment_all(x))
test.to_csv('result.txt', sep='\t', index=None)
