import joblib
import pandas as pd
import numpy as np
import lda
import lda.datasets
import os
import random
from lda_cocurrence.utils import df_groupby_excel

def train_lda(name,topic_k = 20,redo = False):
    if ( not redo ) and os.path.exists('./temp/{}-lda.model'.format(name)):
        return
    word2idx = joblib.load('./temp/{}-word2idx.job'.format(name))
    wordslst = joblib.load('./temp/{}-wordslst.job'.format(name))
    x = len(word2idx)
    y = len(wordslst)
    print('词典大小:{}'.format(x))
    print('文档数量:{}'.format(y))
    docs = np.zeros([y,x])
    for i in range(y):
        for j in range(len(wordslst[i])):
            w = wordslst[i][j]
            if w.strip() == '':
                continue
            if w in word2idx.keys():
                idx = word2idx[w]
                docs[i][idx] = 1

    docs = docs.astype(int)
    count = 0
    ls = []
    #过滤掉一些身上只有低频词的用户
    for i in range(y):
        s = sum(docs[i])
        if s == 0:
            #print(wordslst[i])
            count += 1
        else:
            ls.append(docs[i])
    print('有{}个用户身上只有低频词'.format(count))
    docs = np.array(ls)
    print('参与训练的用户数量：{}'.format(len(docs)))
    #print(docs)
    model = lda.LDA(n_topics=topic_k, n_iter=500, random_state=1)
    model.fit(docs)
    joblib.dump(model,'./temp/{}-lda.model'.format(name))

def test_lda_word(name):
    word2idx = joblib.load('./temp/{}-word2idx.job'.format(name))
    model = joblib.load('./temp/{}-lda.model'.format(name))
    topic_word = model.topic_word_
    word_topic = np.transpose(topic_word)
    #主题个数 * 词典维度 的ndarray
    idx2word = {y: x for x, y in word2idx.items()}
    word_lst = []
    label_lst = []
    word2label = {}
    for x,y in word2idx.items():
        probs = word_topic[y:y+1,:]
        max_topic = np.argmax(probs)
        word2label[x] = max_topic
        word_lst.append(x)
        label_lst.append(max_topic)
    df = pd.DataFrame(np.arange(len(word_lst)))
    df['关键词'] = np.array(word_lst)
    df['LDA主题'] = np.array(label_lst)
    writer = pd.ExcelWriter('./files/word2label.xlsx')
    df.to_excel(writer, encoding='utf-8', index=False, sheet_name='word2label')
    df_groupby_excel(df,'LDA主题','关键词','./files/lda_topic_clusters.xlsx')

#根据MI上的词云和已有的lda类别label去为500个词分类
#都用的qq群数据（用特斯拉上得到的玛莎拉蒂qq群数据训练,MI上的qq群数据分类
#但是有429个词  都没有label，暂时不清楚情况
def classifer_by_lda(filename):
    df = pd.read_excel(filename,sheetname='人群特征')
    word2label = pd.read_excel('./files/word2label.xlsx',sheetname='word2label')
    df = pd.merge(df,word2label,on='关键词',how='left')
    df = df.fillna(-1)
    df_groupby_excel(df, 'LDA主题', '关键词', filename.replace('.xlsx','_lda分类.xlsx'))


#既然没有词云 那就伪造一个吧 随机在词典中选取500个 并分类
def fake_wordcloud():
    word2label = pd.read_excel('./files/word2label.xlsx', sheetname='word2label')
    fake_lst = []
    wordlst = word2label['关键词']
    for i in range(500):
        randidx = int(random.random()*len(wordlst))
        fake_lst.append(wordlst[randidx])
    df = pd.DataFrame(np.arange(500))
    df['关键词'] = np.array(fake_lst)
    df = pd.merge(df, word2label, on='关键词', how='left')
    df = df.fillna(-1)
    df_groupby_excel(df, 'LDA主题', '关键词', './files/fakewordcloud_lda分类.xlsx')


#输出每个主题中最相关的k个词
def test_lda_topic(name):
    word2idx = joblib.load('./temp/{}-word2idx.job'.format(name))
    model = joblib.load('./temp/{}-lda.model'.format(name))
    n = 40
    idx2word = {y:x for x,y in word2idx.items()}
    topic_word = model.topic_word_
    for i, topic_dist in enumerate(topic_word):
        topic_words = []
        l = np.argsort(topic_dist)[:(-n-1):-1]
        for k in range(n):
            topic_words.append(idx2word[l[k]])
        print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))
