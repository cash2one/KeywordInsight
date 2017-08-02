

class KeyWord(object):
    def __init__(self, word, tgi, cover_rate, interest_rate,cate = None):
        self.word = str(word)
        self.tgi = max(tgi, 1)
        self.cover_rate = cover_rate
        self.interest_rate = interest_rate
        self.cate = cate




#根据baike筛选
ls_rule = []
ls_rule.append(['演员','歌手','艺人'])
ls_rule.append(['游戏','手游'])
ls_rule.append(['NBA','球员','篮球'])
ls_rule.append(['电子','数码','手机'])
ls_rule.append(['品牌'])
#ls_rule.append(['汽车','交通','出行'])
#ls_rule.append(['音乐','歌曲','新歌','流行'])
#ls_rule.append(['婴儿','幼儿'])
#ls_rule.append(['购物','促销','超市','生活'])

#根据label筛选
ls2_rule = []
ls2_rule.append(['服饰','鞋','裙'])
#ls_rule.append(['食物','美食','小吃'])
#ls_rule.append(['金融','股票','证券'])
#ls_rule.append(['学习','学校','老师','作业','上课'])

#根据百度筛选
ls3_rule = []
ls3_rule.append(['服饰','鞋','裙'])
#ls_rule.append(['食物','美食','小吃'])
#ls_rule.append(['金融','股票','证券'])
#ls_rule.append(['学习','学校','老师','作业','上课'])
RULE_MAP = {'baike_summary':ls_rule,'baidu_summary':ls3_rule,'label':ls2_rule}