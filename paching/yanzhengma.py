#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author : LTong
# Created on 2019-04-29 : 09:31

from PIL import Image
import pytesseract

file_path = "D:/mr/1.jpg"

img = Image.open(file_path)
print(img)
#
print(pytesseract.image_to_string(img))