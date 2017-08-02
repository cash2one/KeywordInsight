from crawler.crawbywords import crawl
from utils.collectwords import collect
from utils.convertCateID2name import convert
from utils.merge import merge
from utils.prepare_data4_textminer import prepare_data
from word2vector.gettext4word2vector import get_text
from word2vector.word2vec import train,convert_word2vector
import os
import Config
mode = 4
redo = True
if mode == 0:
    # 统计所有可能出现的词提供给爬虫使用
    if redo or not os.path.exists(Config.WORDS_PATH):
        collect()


    # 爬虫 文件保存在temp中
    if redo or not os.path.exists(Config.BAIKE_PATH):
        crawl()

    #准备供textminer分类的数据 文件保存在temp中
    if redo or not os.path.exists(Config.TEXTMINER_FILE):
        prepare_data()

#由于textminer的接口暂时还没有
#所以只能在拿到txt文件后，由samul反馈一个.out文件，并放到temporary文件夹下面。Config中叫 TEXTMINER_FILE

if mode == 1:
    #把.out文件转换为.map文件
    #将samul那边反馈过来的分类文件 格式如 <单词，类别id>的pair，转换成<单词，类别>
    convert()
    #合并文件 把MI上的xlsx merge爬取的结果
    merge()
    #merge完以后就可以根据规则和textminer分类了。


if mode == 2:
    #准备word2vector的训练数据
    if redo or not os.path.exists(Config.WORD2VEC_PATH + 'content.pre'):
        get_text()
    #训练
    if redo or not os.path.exists(Config.WORD2VEC_PATH+'word2vector.model'):
        train()
    #将excel转化成  TensorFlow开源网需要的格式
    convert_word2vector()


from kmeanAnddraw.drawClusterCloud import draw_kmean_clouds
if mode == 3:
    draw_kmean_clouds()

from kmeanAnddraw.drawTextMinerCloud import draw_textminer_classifier_cloud
if mode == 4:
    draw_textminer_classifier_cloud()