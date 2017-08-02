import os

FILE_PATH = '/Users/qiwang/PycharmProjects/KeywordInsight/0802/'

#workspace
WORK_PATH = '/Users/qiwang/PycharmProjects/KeywordInsight/'

#爬虫路径
CRAWL_PATH = WORK_PATH + 'crawler/'

#存放MI上下载下来的xlsx文件
XLSXS_PATH = FILE_PATH + 'xlsxs/'

#临时文件
TEMP_PATH = FILE_PATH + 'temporary/'

WORDS_PATH = TEMP_PATH + 'words.txt'

#爬虫临时文件
BAIDU_PATH = TEMP_PATH + 'baidu.csv'
BAIKE_PATH = TEMP_PATH + 'baike.csv'

#存放merge以后的xlsx文件 也就是给原来的文件，加入一些爬取后的列。
MERGE_PATH = FILE_PATH + 'merge/'


#由samul反馈过来的 分类文件
TEXTMINER_FILE = TEMP_PATH + 'baidu.txt'

#由samul反馈过来的 分类文件
CATEGORY_FILE = TEMP_PATH + 'baidu.txt.out'


#utils path
UTILS_PATH = WORK_PATH+'/utils/'

#word2vec path
WORD2VEC_PATH =FILE_PATH +'word2vec/'

#vectorsAndwords path
VECSANDWORDS_PATH =FILE_PATH +'vecsAndwords/'

#固定文件路径  字体  停用词
CONST_PATH = WORK_PATH+'const_files/'

#图片文件路径
PIC_PATH = FILE_PATH+'pictures/'

#图片文件路径
TEXTMINER_PIC_PATH = FILE_PATH+'pictures/textminer_pics/'

#图片文件路径
KMEANS_PIC_PATH = FILE_PATH+'pictures/kmeans_pics/'

#缓存图片文件路径
TEMP_PIC_PATH = PIC_PATH+'pictemp/'

#一行有多少个小图块
K_PICS = 4

#以excel的方式呈现
RESULT_PATH = FILE_PATH+"results/"

lst = [FILE_PATH,XLSXS_PATH,TEMP_PATH,MERGE_PATH,WORD2VEC_PATH,PIC_PATH,VECSANDWORDS_PATH,
       TEXTMINER_PIC_PATH,KMEANS_PIC_PATH,TEMP_PIC_PATH,RESULT_PATH]
for path in lst:
    if not os.path.exists(path):
        os.mkdir(path)