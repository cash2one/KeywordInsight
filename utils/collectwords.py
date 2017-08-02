
import os
import pandas as pd
import Config

path1 = Config.XLSXS_PATH
path2 = Config.TEMP_PATH

#功能：统计所有可能出现的词提供给爬虫使用
#输入：path下面所有的xlsx文件(MI上获得的所有xlsx文件)
#输出 ：在临时文件夹下面有个words.txt包含所有excel文件出现过的关键词


def collect():
    print('collect words')
    lst = os.listdir(Config.XLSXS_PATH)
    m_set = set()
    for filename in lst:
        df1 = pd.read_excel(Config.XLSXS_PATH+filename, sheetname='人群特征')
        df2 = pd.read_excel(Config.XLSXS_PATH+filename, sheetname='兴趣热度')
        df = pd.merge(df1, df2, how='left', on=['关键词', '覆盖度'])
        for i in range(len(df)):
            word = df.ix[i, 0]
            m_set.add(word)
        print('after add {} total:{}'.format(filename,len(m_set)))

    filename = Config.WORDS_PATH
    f = open(filename,'w',encoding='utf-8')
    for w in m_set:
        f.write(str(w)+'\n')
    f.close()