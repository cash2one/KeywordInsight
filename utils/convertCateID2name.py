

import pandas as pd
import Config

class category(object):
    def __init__(self,a,b,c,d):
        self.first_stage_id = a
        self.first_stage_name = b
        self.second_stage_id = c
        self.second_stage_name = d


class word(object):
    def __init__(self,a,b):
        self.id = a
        self.name = b
        self.category = []
        self.pro = []

#将samul那边反馈过来的分类文件 格式如 <单词，类别id>的pair，转换成<单词，类别>

def convert():
    output_filename = Config.CATEGORY_FILE
    df = pd.read_excel(Config.CONST_PATH+'SPA类目体系汇总.xls',sheetname='SPA商业兴趣V0.3.4.18')
    data = open(output_filename,'r',encoding='utf-8').readlines()
    m_map = {}
    for i in range(0,len(df)):
        a = df.iat[i, 0]
        b = df.iat[i, 1]
        c = df.iat[i, 2]
        d = df.iat[i, 3]
        m_map[int(c)] = category(a,b,c,d)

    m_map[2201] = category(2201,'其他',2201,'其他')
    m_map[7777] = category(7777,'error',7777,'error')
    word_lst = []
    for l in data:
        strs = l.strip().split('\t')
        w = word(strs[0],strs[1])
        if len(strs) == 2:
            w.category.append(m_map[7777])
            w.pro.append(1)
        else:
            strss = strs[2].split(',')
            for t in strss:
                strsss = t.split(':')
                w.category.append(m_map[int(strsss[0])])
                w.pro.append(float(strsss[1]))
        word_lst.append(w)

    f = open(output_filename.replace('txt.out','map'),'w',encoding='utf-8')
    f.write('关键词,一级类目,二级类目')
    f.write('\n')
    for w in word_lst:
        f.write(w.name+',')
        f.write(w.category[0].first_stage_name+",")
        f.write(w.category[0].second_stage_name)
        f.write('\n')
