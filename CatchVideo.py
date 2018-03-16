#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
from tkinter import *
import tkinter.filedialog as tf
#import sys
from PIL import Image


def openfile():
    filename = tf.askopenfilename()
    while filename == '':
        filename = tf.askopenfilename()
    return filename


def faceRec(window_name, camera_idx = 0):

    root.destroy()
    cv2.namedWindow(window_name)

    #开启摄像头
    cap = cv2.VideoCapture(camera_idx)
    if camera_idx == 0:
        fps = 1000
    else:
        fps = cap.get(5)
        print(fps)
    #分类器
    classfier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    #边框颜色
    color = (0,0,255)


    while(1):
        ret, frame = cap.read()

        # 将当前帧灰度化
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(5, 5))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(int(1000/fps)) & 0xff == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    root = Tk()
    def camera():
        faceRec('Video', 0)
    def video():
        faceRec('Video', openfile())
    _button = Button(root, text='摄像头', command = camera)
    _button2 = Button(root, text='选择文件', command = video)
    _button.pack()
    _button2.pack()
    root.mainloop()
