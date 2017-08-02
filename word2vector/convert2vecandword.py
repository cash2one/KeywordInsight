#coding: utf-8
from gensim.models import word2vec


path1 = '../0721/txts/'
path2 = '../0721/vectorsAndwords/'
import os
mode = 0
if mode == 0:

    model = word2vec.Word2Vec.load('../0721/word2vector_min_count5.model')
    lst = os.listdir(path1)
    for filename in lst:
        data = open(path1+filename,'r').readlines()
        f1 = open(path2+filename.replace('txt','word'),'w',encoding='utf-8')
        f2 = open(path2+filename.replace('txt', 'vec'), 'w',encoding='utf-8')
        for w in data:
            w = w.strip().lower()
            strs = w.split('/')
            w = strs[0]
            print(w)
            if w in model.wv.vocab.keys():
                f1.write(w+'/'+strs[1]+'\n')
                for v in model[w]:
                    f2.write(str(v))
                    f2.write('\t')
                f2.write('\n')
        f1.close()
        f2.close()

