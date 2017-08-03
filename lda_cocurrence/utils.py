import pandas as pd
import numpy as np



#一个dataframe  根据一个key 分组，将字段  输出到文件中去
def df_groupby_excel(df,key,field,filename):
    clusters = {}
    groups = dict(list(df.groupby(key)))
    maxlen = 0
    for x, y in groups.items():
        lst = y.reset_index()[field]
        clusters[x] = lst
        maxlen = max(maxlen,len(lst))

    writer = pd.ExcelWriter(filename)
    res = pd.DataFrame(np.arange(maxlen))
    for x, y in clusters.items():
        res[x] = y
    res.to_excel(writer, encoding='utf-8', index=False, sheet_name='lda')
    writer.save()