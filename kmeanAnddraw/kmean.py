import Config
from kmeanAnddraw.draw_wcloud import draw_word_cloud_base
from gensim.models import word2vec
from sklearn.cluster import KMeans
import kmeanAnddraw.drawPic as dr

path1 = '../txts/'
path2 = '../vectorsAndwords/'
import os

pic_path =Config.PIC_PATH


def do_kmeans(keywords,modelname,K,filename):
    model = word2vec.Word2Vec.load(modelname)
    lst = []
    error = []
    for w in keywords:
        word = w.word.strip().lower()
        if word in model.wv.vocab.keys():
            lst.append(w)
        else:
            error.append(w)
    X = model[[w.word.strip().lower() for w in lst]]
    y_pred = KMeans(K, random_state=9).fit_predict(X)

    #将聚类结果分开写入到png中  然后merge为一张大图
    y = y_pred.tolist()
    clusters = []
    for i in range(K):
        clusters.append([])
    for i in range(len(y)):
        clusters[y[i]].append(lst[i])
    print('draw cloud')
    clusters.append(error)



    map1 = {}
    map2 = {}
    for i in range(K+1):
        l = {x.word: x.tgi for x in clusters[i]}
        fname = Config.TEMP_PIC_PATH+'{}.png'.format(i)
        draw_word_cloud_base(l, fname)
        map1[fname] = '类别{}'.format(i)
        map2['类别{}'.format(i)] = clusters[i]
    map1[fname] = 'error'

    dr.merge_pic(map1,Config.KMEANS_PIC_PATH+filename.replace('.xlsx','{}.png'.format(len(y))))
    return map2