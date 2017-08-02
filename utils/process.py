from tqdm import tqdm
import pandas as pd
df = pd.read_excel('./keywords/app.xlsx',sheetname='sheet1')
wordlst = []
for i in range(1,len(df)):
    word = df.ix[i,0]
    wordlst.append(word)

#统计词云中的500个词在这群人身上的覆盖度，兴趣度的平均值

class kword(object):
    def __init__(self,word):
        self.word = word
        self.user_count = 0
        self.interest = []

    def add(self,interest_rate):
        self.user_count += 1
        self.interest.append(float(interest_rate))

    def get_interest(self):
        total = 0.0
        for rate in self.interest:
            total += rate
        return total/len(self.interest)

filename = 'dd-adclick'
m_map = {}
data = open(filename,'r',encoding='utf-8').readlines()
for oneline in tqdm(data):
    onelines = oneline.split('#')
    qq = oneline[0]
    if(oneline[1].strip()==''):
        continue
    words = onelines[1].split(',')
    for w in words:
        if (w.strip() == ''):
            continue
        w1 = w.split('/')[0]
        w2 = w.split('/')[1].split(':')[1]
        if not w1 in m_map:
            m_map[w1] = kword(w1)
        m_map[w1].add(w2)
print(len(data))
lst = []
for w in wordlst:
    if w in m_map.keys():
        lst.append(m_map[w])
print(len(lst))
print(float(len(lst))/len(wordlst))
print('???')
lst = sorted(lst,key=lambda x:x.user_count)
for x in lst:
    print(x.word,x.user_count)
