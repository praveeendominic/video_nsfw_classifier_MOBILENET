import streamlit as st
import os

import pathlib
from pathlib import Path
from nsfw_detector import predict
from tensorflow import keras
import numpy as np
from PIL import Image

import cv2


result=''
model_path = Path('model_mobilenet')/ 'saved_model.h5'
model=predict.load_model(model_path)


st.header('VIDEO NUDITY DETECTOR')
st.write("Please select a video for nudity check.")

video_uploaded=st.file_uploader(label= "Please upload a file",accept_multiple_files=False, type = ['mp4','.wmv'])
if video_uploaded is not None:
    st.video(video_uploaded)

    fname=os.path.splitext(video_uploaded.name)
    file_ext=fname[1]
    fname_u='tmp'+file_ext
  
    # saving file
    with open(fname_u, 'wb') as f:
        f.write(video_uploaded.getbuffer())
        st.success("File upload complete..")

    
    import cv2 
    result=""
    fres={}

    def video_nsfw(video_path):
    # c=0
        vidcap = cv2.VideoCapture(video_path) 
        # flag=''
        def getFrame(sec,flag=''): 
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
            hasFrames,frame = vidcap.read() 
            if hasFrames: 
                im=Image.fromarray(frame).resize((224,224))
                image = keras.preprocessing.image.img_to_array(im)
                image /=255
                image=np.expand_dims(image,axis=0)
                res=predict.classify_nd(model,image)[0]
                if ((res.get('porn')>0.7) or (res.get('sexy')>0.7) or (res.get('hentai')>0.6)):      
                    flag='x'
                    # print(res)
                    # cv2_imshow(frame)
                    hasFrames=False
                # cv2.waitKey(0)
                # return (False, flag)
                # cv2.imwrite("frame "+str(sec)+" sec.jpg", image)     # save frame as JPG file 
            return (hasFrames, flag)
            # return hasFrames 
        sec = 0 
        frameRate = 3#it will capture image in each 0.5 second 
        success = getFrame(sec) 
        # print(success)
        while success: 
            sec = sec + frameRate 
            sec = round(sec, 3) 
            success, fl = getFrame(sec) 
            # print(sec)
            # print(fl)
            if fl=='x':
                return "nsfw"
                # break
        else:
            return 'safe'


    # def video_nsfw_detector(video_path):
    #     videodata=cv2.VideoCapture(video_path)
    #     flag=''
    #     while(videodata.isOpened()):
    #         ret, frame = videodata.read()
    #         if ret == True:
    #             im=Image.fromarray(frame).resize((224,224))
    #             image = keras.preprocessing.image.img_to_array(im)
    #             image /=255
    #             image=np.expand_dims(image,axis=0)
    #             res=predict.classify_nd(model,image)[0]
    #             if ((res.get('porn')>0.7) or (res.get('sexy')>0.7) or (res.get('hentai')>0.5)):
    #                 flag='x'
    #                 break
    #             else:
    #                 flag = ''
    #     if flag!='x':
    #         result="Video is safe for publishing!"
    #     else:
    #         result=f"Obscene content detected"

    #     return result

    import time
    with st.spinner('Wait for it...'):
        time.sleep(5)

        result = video_nsfw(fname_u)
        # st.write(result)

        if result=="Video is safe for publishing!":
            st.success("Video is safe for publishing!")
        else:
            st.error(result)
            

        