from tqdm import tqdm
import joblib
import queue
name = 'dd'


class KeyWord(object):
    def __init__(self,word):
        self.word = word
        self.cocur_words = {}
        self.count = 0

#定义两个关键词的相似度
def get_similarity(count1,count2,cocurrence):
    if cocurrence <= 2:
        return 0
    #a2b = cocurrence / count1
    #b2a = cocurrence / count2
    aAndb = cocurrence * 2 / (count1 + count2)
    #return a2b + b2a + aAndb
    return aAndb

class CoInSight(object):
    def __init__(self):
        self.vocab = joblib.load('./temp/{}-vocab.job'.format(name))
        self.qq2keywords = joblib.load('./temp/{}-qq2keywords.job'.format(name))
        for lst in tqdm(self.qq2keywords):
            for w1 in lst:
                for w2 in lst:
                    if w1 == w2:
                        continue
                    word1 = self.vocab[w1]
                    word2 = self.vocab[w2]
                    map1 = self.vocab[w1].cocur_words
                    co_count = 1
                    if w2 in map1:
                        co_count = map1.get(w2) + 1
                    map1[w2] = co_count


    #洞察某个关键词，输出与其相近的词
    def capture(self,word,show = True):
        word1 = self.vocab[word]
        cand_words = word1.cocur_words
        map4sort = {x:get_similarity(word1.count,self.vocab[x].count,y) for x,y in cand_words.items()}
        d2 = sorted(map4sort.items(), key=lambda x: x[1], reverse=True)
        if show :
            print()
            print(word)
            for w in d2[:10]:
                print('{}:{}'.format(w[0],str(w[1])[:4]))
        return [x[0] for x in d2]

    #根据一个中心词扩展出与其直接相关和间接相关的词
    def generate_cluster(self,word,show = True):
        ret1 = []
        ret2 = []
        q = queue.Queue()
        q.put((word,0))
        while not q.empty():
            a = q.get()
            if(a[1] == 4):
                break
            if not a[0] in ret1:
                ret1.append(a[0])
                ret2.append(a)
            lst = self.capture(a[0],show=False)
            #limit = 10 限制只将与其最相关的10个词放入队列
            for w in lst[:10]:
                q.put((w,a[1]+1))

        i = 0
        if show:
            cand = 0
            for w in ret2:
                if w[1] != cand:
                    print()
                    cand = w[1]
                print(w[0],end=',')
                i+=1
            print()
        return ret2


if __name__ == '__main__':
    mode = 1
    if mode == 1:
        cis = CoInSight()
        mode2 = 1
        words = list(cis.vocab.keys())
        if mode2 == 1:
            cis.generate_cluster('奔驰')
            print('===' * 50)
            cis.generate_cluster('王者荣耀')
            print('===' * 50)
            cis.generate_cluster('苹果')
            print('===' * 50)
            cis.generate_cluster('君威')
            print('===' * 50)
            cis.generate_cluster('玛莎拉蒂')
            print('===' * 50)
            cis.generate_cluster('奥迪')
            print('===' * 50)
            cis.generate_cluster('丰田')
            print('===' * 50)
            cis.generate_cluster('二手车')
            print('===' * 50)
            cis.generate_cluster('奢侈品')
        if mode2 == 0:

            #print(len(words))
            # import random
            # for i in range(50):
            #     w = words[int(random.random() * len(words))]
            #     capture(w)
            #     print('==='*10)
            cis.capture('高尔夫')
            cis.capture('英雄联盟')
            cis.capture('王者荣耀')
            cis.capture('炉石传说')
            cis.capture('苹果')
            cis.capture('找对象')
            cis.capture('单身交友')
            cis.capture('头等舱')
            cis.capture('特价机票')
            cis.capture('二手车')
            cis.capture('玛莎拉蒂')
            cis.capture('宝马')
            cis.capture('奔驰')
            cis.capture('沃尔沃')
            cis.capture('丰田')
            cis.capture('迈腾')
            cis.capture('大众')
            cis.capture('君威')
            cis.capture('朗逸')
            cis.capture('奢侈品')
            #cis.capture('按揭购车')
            cis.capture('租车')
            cis.capture('携程')
            cis.capture('渔具')
            cis.capture('自驾游')
            cis.capture('旅游')
            cis.capture('改装')
            #cis.capture('携程旅行')

            # cis.capture('烤鱼')
            # cis.capture('火锅')
            # cis.capture('美团')
            # cis.capture('外卖')
            # cis.capture('考研')
    print('???')

