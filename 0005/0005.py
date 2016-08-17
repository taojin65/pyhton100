#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os

from PIL import Image

def image_sf(file, a = 100, b = 200):
	im = Image.open(file)
	(x, y) = im.size
	vga_photo = x * y
	vga_ip5 = a * b
	if vga_photo > vga_ip5:
		t = ((vga_photo/vga_ip5) + 1)
		x_new = x / t
		y_new = y / t
		im_new = im.resize((x_new,y_new),Image.ANTIALIAS)
		im_new.save('touxiang_new.png', 'png')


image_sf('touxiang.png')

