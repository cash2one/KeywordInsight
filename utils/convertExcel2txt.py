path = './files/'
import os
import pandas as pd
lst = os.listdir(path)



for filename in lst:
    f = open('./txts/'+filename.replace('xlsx','txt'), 'w', encoding='utf-8')
    df1 = pd.read_excel('./files/'+filename, sheetname='人群特征')
    df2 = pd.read_excel('./files/'+filename, sheetname='兴趣热度')
    df = pd.merge(df1, df2, how='left', on=['关键词', '覆盖度'])
    for i in range(len(df)):
        w = df.ix[i, 0]
        f.write(w + '\n')
    f.close()