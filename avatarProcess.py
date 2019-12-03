#!/usr/bin/env python3
# coding=utf-8

import cv2
import os


def type_convert(filename):
    pngname = '/'.join(filename.split('/')[0:-1]) + '/' + filename.split('/')[-1].split('.')[0] + '.png'
    print(filename, pngname)
    img = cv2.imread(filename)
    cv2.imwrite(pngname, img)


if __name__ == "__main__":
    path = r'./testimg'
    files = [path+'/'+x for x in os.listdir(r'./testimg')]
    for file in files:
        type_convert('./testimg/无标题.bmp')