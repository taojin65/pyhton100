#!/usr/bin/python
# -*- coding: UTF-8 -*- 


from PIL import Image, ImageDraw, ImageFont

ttfont = ImageFont.truetype('Arial.ttf', 100)
im = Image.open("touxiang.png")
draw = ImageDraw.Draw(im)
draw.text((240,5), '4', fill=(220,20,60), font=ttfont)
im.show()