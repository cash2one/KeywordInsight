from PIL import Image,ImageDraw,ImageFont
import Config

#一行多少个图块
K = Config.K_PICS


def merge_pic(map1 , save_path):
    ttfont = ImageFont.truetype(Config.CONST_PATH+"HYQiHei-25JF.ttf", 20)
    i = 0
    split1 = Image.open(Config.CONST_PATH+'split.png')
    split2 = Image.open(Config.CONST_PATH+'split2.png')
    split1 = split1.resize((15,1025))
    split2 = split2.resize((K*1000 + (K-1)*15, 15))
    pics = []
    toImage = Image.new('RGBA',(K*1000 + (K-1)*15,1025),color='white')
    for pic_name, cate_name in map1.items():
        im1 = Image.open(pic_name)
        xsize, ysize = im1.size
        im2 = Image.new('RGBA', (xsize, 25 + ysize), color='white')
        im2.paste(im1, (0, 25))
        draw = ImageDraw.Draw(im2)
        draw.text((0, 0), cate_name, fill=(0, 0, 0), font=ttfont)
        toImage.paste(im2, (i * 1015, 0))
        if i == K-1:
            pics.append(toImage)
            toImage.save(Config.TEMP_PIC_PATH+'temp{}.png'.format(i))
            toImage = Image.new('RGBA', (K*1000 + (K-1)*15, 1000),color='white')
            i = 0
        else:
            toImage.paste(split1, (i * 1015 + 1000, 0))
            i += 1
    if i != 0:
        pics.append(toImage)

    res = Image.new('RGBA',(1000*K,1000*len(pics)+(len(pics)-1)*15))
    i = 0
    for pic in pics:
        pic = pic.resize((1000*K,1000))
        res.paste(pic,(0,i*1015))
        if i != len(pics)-1:
            res.paste(split2, (0, i*1015+1000))
        i += 1
    print('merge picture')
    res.save(save_path)



