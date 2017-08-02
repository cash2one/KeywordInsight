
from gensim.models import word2vec
import logging
import Config
import pandas as pd
import os

def train():
    filename2 = "content.pre"
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(Config.WORD2VEC_PATH + filename2)  # 加载语料
    model = word2vec.Word2Vec(sentences, size=200,iter=20)  # 训练skip-gram模型; 默认window=5
    # 保存模型，以便重用
    model.save(Config.WORD2VEC_PATH+'word2vector.model')

#转换成TensorFlow可视化格式
def convert_word2vector():

    model = word2vec.Word2Vec.load(Config.WORD2VEC_PATH+'word2vector.model')
    path1 = Config.XLSXS_PATH
    path2 = Config.VECSANDWORDS_PATH
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
            data.append(str(w1) + '/' + str(w2) + '/' + str(w3) + '/' + str(w4))

        f1 = open(path2+filename.replace('xlsx','word'),'w',encoding='utf-8')
        f2 = open(path2+filename.replace('xlsx', 'vec'), 'w',encoding='utf-8')
        for w in data:
            w = w.strip().lower()
            strs = w.split('/')
            w = strs[0]
            if w in model.wv.vocab.keys():
                f1.write(w+'/'+strs[1]+'\n')  #只保留词和tgi
                for v in model[w]:
                    f2.write(str(v))
                    f2.write('\t')
                f2.write('\n')
        f1.close()
        f2.close()

