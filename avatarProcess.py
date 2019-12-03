#!/usr/bin/env python3
# coding=utf-8

import cv2
import os
import base64
from db_conn import get_db


def type_convert(filename):
    pngname = '/'.join(filename.split('/')[0:-1]) + '/' + filename.split('/')[-1].split('.')[0] + '.png'
    print(filename, pngname)
    img = cv2.imread(filename)
    cv2.imwrite(pngname, img)

def insert_img(filename):
    id = filename.split('/')[-1].split('.')[0]
    db = get_db()
    with open(filename, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        db.excute('UPDATE TABLE person SET picture=? WHERE id=?', ('data:image/png;base64,%s'%s, id))


if __name__ == "__main__":
    path = r'./testimg'
    files = [path+'/'+x for x in os.listdir(r'./testimg')]
    for file in files:
        type_convert('./testimg/无标题.bmp')