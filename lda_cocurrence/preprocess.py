from lda_cocurrence.cocurrenceInsight import KeyWord
from tqdm import tqdm
import joblib
import os

#词共现实验需要准备 词-词频映射关系map<word(str),count(int)> 每个qq上面的身上的所有关键词 list<qq(str),keywords(list)>
def cocurrence_process(name,redo = False):
    if ( not redo ) and os.path.exists('./temp/{}-vocab.job'.format(name)):
        return
    filename = './files/{}-qqgroup'.format(name)
    data = open(filename, 'r', encoding='utf-8').readlines()
    qq2keywords = []
    vocab = {}
    for oneline in tqdm(data):
        onelines = oneline.split('#')
        #qq = oneline[0]
        #有用户身上没有关键词
        if (oneline[1].strip() == ''):
            continue
        words = onelines[1].split(',')
        wordlst = []
        # 词共现在main函数中实现，因为如果先把共现关系保存到数据结构，用joblib保存太慢，还不如直接计算
        for w in words:
            if (w.strip() == ''):
                continue
            w1 = w.split('/')[0]
            wordlst.append(w1)
            if w1 not in vocab.keys():
                vocab[w1] = KeyWord(w1)
            vocab[w1].count += 1
        qq2keywords.append(wordlst)
    joblib.dump(vocab,'./temp/{}-vocab.job'.format(name))
    joblib.dump(qq2keywords,'./temp/{}-qq2keywords.job'.format(name))


#lda 需要把低频词去掉（高频词也可以去掉），然后准备  词-id的映射。准备 文档的onehot表示
def lda_process(name,redo = False):
    if ( not redo ) and os.path.exists('./temp/{}-word2idx.job'.format(name)):
        return
    filename = './files/{}-qqgroup'.format(name)
    data = open(filename, 'r', encoding='utf-8').readlines()
    qq2keywords = []
    vocab = {}
    #统计词频和 qq-keyword映射
    for oneline in tqdm(data):
        onelines = oneline.split('#')
        #去掉没有关键词的用户
        if (onelines[1].strip() == ''):
            continue
        words = onelines[1].split(',')
        wordlst = []
        for w in words:
            w1 = w.split('/')[0]
            wordlst.append(w1)
            if w1 not in vocab.keys():
                vocab[w1] = 1
            else:
                vocab[w1] += 1

        qq2keywords.append(wordlst)
    id = 0
    vocab_after_pre = {}
    #l = sorted(vocab.items(),reverse = True,key = lambda x:x[1])
    for x, y in vocab.items():
        if y > 2:
            vocab_after_pre[x] = id
            id += 1

    joblib.dump(vocab_after_pre, './temp/{}-word2idx.job'.format(name))
    joblib.dump(qq2keywords, './temp/{}-wordslst.job'.format(name))