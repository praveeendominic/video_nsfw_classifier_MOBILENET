
from nsfw_detector import predict
# pthlb = Path('ffmpeg') / 'bin'
# # ffmpeg_path = "C:\\code\\justo_nudity_classifier\\ffmpeg\\bin"


# import os.path
# ffmpeg_path = os.path.join('ffmpeg','bin')


# # model_path = Path('model_mobilenet')/ 'saved_model.h5'
# print(ffmpeg_path)
# print(pthlb)

import pathlib
from pathlib import Path

import skvideo
import skvideo.io
import os.path
import numpy as np
from PIL import Image
from tensorflow import keras
# ffmpeg_path_os = os.path.join('ffmpeg','bin')
# ffmpeg_path_pthlib = Path('ffmpeg') / 'bin'

# print(ffmpeg_path_os)
# print(ffmpeg_path_pthlib)
# model_path = Path('model_mobilenet')/ 'saved_model.h5'
# print(model_path)
# skvideo.setFFmpegPath(ffmpeg_path_os)
# import skvideo.io


# videodata = skvideo.io.vread("C:\\code\\video nudity detector app\\tmp.mp4")

import sys
import skvideo.io
import cv2
# vd=skvideo.io.vreader("C:\\code\\video nudity detector app\\tmp.mp4")

vid = cv2.VideoCapture("C:\\code\\video nudity detector app\\tmp.mp4")
while(True):
    ret, frame = vid.read()
    im=Image.fromarray(frame).resize((224,224))
    image = keras.preprocessing.image.img_to_array(im)
    image /=255
    image=np.expand_dims(image,axis=0)
    print(image.shape)

    # print(frame)
    # print(frame.shape)
    break


# for frame in vd:
#     print(frame.shape)
#     im=Image.fromarray(frame).resize((224,224))
#     image = keras.preprocessing.image.img_to_array(im)
#     image /=255
#     image=np.expand_dims(image,axis=0)
#     print(image.shape)
#     break

# flag=''
# frame_num=0
# for i in range(len(videodata)):
#     frame = videodata[i]
#     print(frame)
#     print(frame.shape)

    # im=Image.fromarray(frame).resize((224,224))
#     image = keras.preprocessing.image.img_to_array(im)
#     image /=255
#     image=np.expand_dims(image,axis=0)
#     print(image.shape)
# #     break

