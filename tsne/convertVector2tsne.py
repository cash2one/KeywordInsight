import Config
import os
from sklearn.manifold import TSNE
import numpy as np
from gensim.models import word2vec
import pandas as pd
path = Config.VECSANDWORDS_PATH
lst = os.listdir(path)

class KeyWord4TSNE(object):
    def __init__(self, word, tgi, cover_rate, interest_rate,vector):
        self.word = str(word)
        self.tgi = max(tgi, 1)
        self.cover_rate = cover_rate
        self.interest_rate = interest_rate
        self.vec = vector

def convert_word2vector():
    model = word2vec.Word2Vec.load(Config.WORD2VEC_PATH+'word2vector.model')
    path1 = Config.XLSXS_PATH
    lst = os.listdir(path1)
    for filename in lst:
        #将excel中的词和其tgi提出来
        df1 = pd.read_excel(path1 + filename, sheetname='人群特征')
        df2 = pd.read_excel(path1 + filename, sheetname='兴趣热度')
        df = pd.merge(df1, df2, how='left', on=['关键词', '覆盖度'])
        data = []
        for i in range(len(df)):
            w1 = df.ix[i, 0]
            w2 = df.ix[i, 1]
            w3 = df.ix[i, 2]
            w4 = df.ix[i, 3]
            vec = model[w1] if w1 in model.wv.vocab.keys() else None
            if not vec is None:
                data.append(KeyWord4TSNE(w1,w2,w3,w4,vec))
        print(len(data))
        lst = [x.vec for x in data]
        x_3d = TSNE(n_components=3,perplexity=6,learning_rate=10,n_iter=800).fit_transform(np.array(lst))
        df = df[df['关键词'].apply(lambda x : x in model.wv.vocab.keys())]
        df['x_0'] = x_3d[:, 0]
        df['x_1'] = x_3d[:, 1]
        df['x_2'] = x_3d[:, 2]
        writer = pd.ExcelWriter(Config.TSNE_PATH+filename.replace('.xlsx','_tsne.xlsx'))
        df.to_excel(writer, encoding='utf-8', index=False, sheet_name='sheet1')
        writer.save()


if __name__ == '__main__':
    convert_word2vector()