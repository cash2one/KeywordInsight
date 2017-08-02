
import os
import Config
from kmeanAnddraw.drawPic import merge_pic
from kmeanAnddraw.draw_wcloud import draw_word_cloud_base
from kmeanAnddraw.keyword import KeyWord,RULE_MAP


def draw_textminer_classifier_cloud(mode = 6,output_format = 6):
    lst = os.listdir(Config.MERGE_PATH)
    import pandas as pd
    for filename in lst:
        print('process:{}'.format(filename))
        df = pd.read_excel(Config.MERGE_PATH + filename,encoding='utf-8')

        clusters = {}
        if mode % 3 == 0:
            now_rule = None
            def rule(str1):
                for w in now_rule:
                    if w in str(str1):
                        return True
                return False

            for attr,ls_rule in RULE_MAP.items():
                for y in ls_rule:
                    now_rule = y
                    rule_name = '-'.join(now_rule)
                    df[rule_name] = df[attr].apply(rule) | df['关键词'].apply(rule)
                    y = df[df[rule_name]]
                    df = df[~df[rule_name]]
                    lst = []
                    y = y[['关键词', '人群特征（TGI）', '覆盖度', '兴趣热度']]
                    for i in range(len(y)):
                        y = y.reset_index().iloc[:, 1:]
                        word = KeyWord(y.ix[i, 0], y.ix[i, 1], y.ix[i, 2], y.ix[i, 3])
                        lst.append(word)
                    if len(lst) != 0:
                        clusters[rule_name] = lst

        print('after rules remain : {}'.format(len(df)))

        if mode % 2 == 0:
            df = df[['关键词', '人群特征（TGI）', '覆盖度', '兴趣热度', '一级类目']]
            groups = dict(list(df.groupby('一级类目')))
            for x, y in groups.items():
                lst = []
                for i in range(len(y)):
                    y = y.reset_index().iloc[:,1:]
                    word = KeyWord(y.ix[i, 0], y.ix[i, 1], y.ix[i, 2], y.ix[i, 3])
                    lst.append(word)
                clusters[x] = lst

        if output_format % 2 == 0:
            import pandas as pd
            import numpy as np
            writer = pd.ExcelWriter(Config.RESULT_PATH+filename.replace('.xlsx','分类.xlsx'))
            res = pd.DataFrame(np.arange(500))
            for x, y in clusters.items():
                res[x] = pd.DataFrame(np.array(['{}/{}'.format(k.word,k.tgi) for k in y]))
            res.to_excel(writer, encoding='utf-8', index=False, sheet_name=filename)
            writer.save()

        if output_format % 3 == 0:
            map1 = {}
            i = 0
            for x,y in clusters.items():
                l = {x.word: x.tgi for x in y}
                fname = Config.TEMP_PIC_PATH+'/{}.png'.format(i)
                i += 1
                draw_word_cloud_base(l, fname)
                map1[fname] = x
            merge_pic(map1,Config.TEXTMINER_PIC_PATH+filename.replace('.xlsx','.png'))






