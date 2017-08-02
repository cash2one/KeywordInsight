
# 生成word2vector的训练语料和textminer的分类语料
import Config
import pandas as pd
import jieba


def get_text():
    #获取数据
    print('get text for word2vector')
    dict1 = pd.read_csv(Config.BAIDU_PATH)
    dict1['关键词'] = dict1['word']
    dict1 = dict1[['关键词','baidu_summary']]
    dict2 = pd.read_csv(Config.BAIKE_PATH)
    dict2['关键词'] = dict2['old_word']
    dict2 = dict2[['关键词','baike_summary']]

    df = pd.merge(dict1,dict2,how='left',on='关键词')
    df = df.fillna('')
    data = []
    for x,y in zip(df['baike_summary'],df['baidu_summary']):
        data.append(x.strip())
        data.append(y.strip())

    # 分词
    # 去除停用词
    print('word seg')
    jieba.load_userdict(Config.WORDS_PATH)
    stopwords = {x.strip() for x in open(Config.CONST_PATH + 'stopword', 'r').readlines()}
    writer = open(Config.WORD2VEC_PATH + 'content.pre', 'w')
    for l in data:
        seg_list = jieba.cut(l)
        new_seg = [x for x in seg_list if x not in stopwords]
        new_seg = [x.lower() for x in new_seg if x.strip() != '']
        writer.write(" ".join(new_seg) + '\n')
    writer.close()




