#coding:utf-8

import os
import pandas as pd
import Config


def merge():
    print('merge file')
    lst = os.listdir(Config.XLSXS_PATH)
    dict1 = pd.read_csv(Config.BAIDU_PATH)
    dict1['关键词'] = dict1['word']
    #dict1['baidu_summary'] = dict1['summary']
    dict1 = dict1[['关键词','baidu_summary','label']]
    dict2 = pd.read_csv(Config.BAIKE_PATH)
    dict2['关键词'] = dict2['old_word']
    #dict2['baike_summary'] = dict2['summary']
    dict2 = dict2[['关键词','baike_summary']]
    dict3 = pd.read_csv(Config.TEMP_PATH+'baidu.map')
    for filename in lst:
        df1 = pd.read_excel(Config.XLSXS_PATH+filename, sheetname='人群特征')
        df2 = pd.read_excel(Config.XLSXS_PATH+filename, sheetname='兴趣热度')
        df = pd.merge(df1, df2, how='left', on=['关键词', '覆盖度'])
        df = pd.merge(df,dict1,how='left',on=['关键词'])
        df = pd.merge(df,dict2,how='left',on=['关键词'])
        df = pd.merge(df, dict3, how='left', on=['关键词'])
        df.to_excel(Config.MERGE_PATH+filename,encoding='utf-8')
