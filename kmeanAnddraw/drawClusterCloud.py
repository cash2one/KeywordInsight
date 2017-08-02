
import os
from kmeanAnddraw.kmean import do_kmeans
import Config
from kmeanAnddraw.keyword import KeyWord

path = Config.XLSXS_PATH
modelname = Config.WORD2VEC_PATH+'word2vector.model'


def draw_kmean_clouds(output_format = 2):
    lst = os.listdir(path)
    import pandas as pd
    for filename in lst:
        print('process:{}'.format(filename))
        df1 = pd.read_excel(path+filename, sheetname='人群特征')
        df2 = pd.read_excel(path+filename, sheetname='兴趣热度')
        df = pd.merge(df1, df2, how='left', on=['关键词', '覆盖度'])
        df1 = df[['关键词','人群特征（TGI）','覆盖度','兴趣热度']]
        lst = []
        for i in range(len(df1)):
            word = KeyWord(df1.ix[i, 0],df1.ix[i, 1],df1.ix[i, 2],df1.ix[i, 3])
            lst.append(word)
        map1 = do_kmeans(lst,modelname,8,filename)

        if output_format % 2 == 0:
            import pandas as pd
            import numpy as np
            writer = pd.ExcelWriter(Config.RESULT_PATH+filename.replace('.xlsx','聚类.xlsx'))
            res = pd.DataFrame(np.arange(500))
            for x, y in map1.items():
                res[x] = pd.DataFrame(np.array(['{}/{}'.format(k.word,k.tgi) for k in y]))
            res.to_excel(writer, encoding='utf-8', index=False, sheet_name=filename)
            writer.save()



