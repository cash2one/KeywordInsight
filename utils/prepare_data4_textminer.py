
import pandas as pd
import Config
#将csv文件转成txt 供textminer分类


def prepare_data():
    print('prepare data for textminer')
    filename = Config.BAIDU_PATH
    df = pd.read_csv(filename)
    writer = open(filename.replace('csv','txt'),'w')
    df = df.fillna('')
    for i in range(1,len(df)):
        s = df.iloc[i]['baidu_summary'].replace('\n','').strip()
        w = df.iloc[i]['word']
        if s != '':
            writer.write(str(i)+'\t'+w+'\t')
            writer.write(s)
            writer.write('\n')
    writer.close()