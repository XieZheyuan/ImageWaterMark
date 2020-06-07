#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont, ImageFilter



def insert_text(text, fone_type_file, font_size, im, position, color, fn):
    '''
    ** text 要插入的文字
    ** fone_type_file 文字类型文件名称
    ** font_size 文字大小
    ** im 背景图片
    ** position 要插入的位置
    '''

    datas = text.split('\n')
    data = ''
    if not datas:
        datas = [text]
    for d in datas:
        if not d:
            d = ' '
        elif len(d) > 31:
            d1 = d[:30] + '\n'
            d2 = d[30:]
            d = d1 + ' \n' + d2
        data += (d + '\n')
        data += ' \n'

    data = data[:-1]
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(fone_type_file, font_size)

    dr.text(position, data, font=font, fill=color, spacing=0, align='left')
    im.save(fn)
    return im, len(datas)


s = input("WaterMark String:\n")
i = input("Source Image Path:(Default:eg/4.jpg)\n")
if i.strip() == "":
    i = "eg/4.jpg"
c = input("Hex Color:(Default:#32CD32)\n")
if c.strip() == "":
    c = "#32CD32"
p = input("Will Save Image Path:(Default:original)\n")
if p.strip() == "":
    p = i
l = input("Size:(Default:128)\n")
if l.strip() == "":
    l = 128
else:
    l=int(l)
f = input("Font:(c/j)(Default:j):\n")
if f == "c":
     f = "fonts/comic.ttf"
else:
    f = "fonts/jet.ttf"
insert_text(s, f, l, Image.open(i), [200, 200], c, p)