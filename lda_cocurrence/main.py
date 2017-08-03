from lda_cocurrence.cocurrenceInsight import CoInSight
from lda_cocurrence.preprocess import cocurrence_process,lda_process
from lda_cocurrence.lda_experiment import train_lda,test_lda_word,classifer_by_lda,fake_wordcloud
#name = 'dd' or 'msld'
if __name__ == '__main__':
    mode = 1
    if mode == 0:
        cocurrence_process('dd')
        cis = CoInSight()
        cis.capture('苹果')
        cis.generate_cluster('大众')

    if mode == 1:
        name = 'msld'
        lda_process(name)
        train_lda(name,redo=False)
        test_lda_word(name)
        #classifer_by_lda('./files/玛莎拉蒂车主终板qq群.xlsx')
        fake_wordcloud()