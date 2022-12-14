
import streamlit as st
import os

import pathlib
from pathlib import Path
from nsfw_detector import predict
from tensorflow import keras
import numpy as np
from PIL import Image

import skvideo

#Path('ffmpeg') / 'bin'#
# Path('ffmpeg') / 'bin' #
import os.path
ffmpeg_path = os.path.join('ffmpeg','bin')
# ffmpeg_path = "C:\\code\\justo_nudity_classifier\\ffmpeg\\bin"
skvideo.setFFmpegPath(ffmpeg_path)
import skvideo.io


result=''
model_path = Path('model_mobilenet')/ 'saved_model.h5'
model=predict.load_model(model_path)


st.header('VIDEO NUDITY DETECTOR')
st.write("Please select a video for nudity check.")

video_uploaded=st.file_uploader(label= "Please upload a file",accept_multiple_files=False, type = ['mp4'])
if video_uploaded is not None:
    st.video(video_uploaded)
    # st.write(video_uploaded.name)

    # uploaded_image_path=os.path.join('tmp_dir',image_uploaded.name)
    # st.write(uploaded_image_path)
    fname=os.path.splitext(video_uploaded.name)
    file_ext=fname[1]
    # st.write(file_ext)
    fname_u='tmp'+file_ext
    # st.write(fname_u)
    
    # saving file
    with open(fname_u, 'wb') as f:
        f.write(video_uploaded.getbuffer())
        st.success("File upload complete..")


    def video_nsfw_detector(video_path):
        videodata = skvideo.io.vread(video_path)
        flag=''
        frame_num=0
        for i in range(len(videodata)):
            frame = videodata[i]
            im=Image.fromarray(frame).resize((224,224))
            image = keras.preprocessing.image.img_to_array(im)
            image /=255
            image=np.expand_dims(image,axis=0)

            res=predict.classify_nd(model,image)[0]
            # print(res)
            if ((res.get('porn')>0.7) or (res.get('sexy')>0.7) or (res.get('hentai')>0.5)):
                flag='x'
                frame_num=i
                # print(f"@frame: {i}")
                # print(res)
                # print("Obscene content detected!")
                # cv2.imshow(frame)
                break
            
        if flag!='x':
            # print("Video is safe for publishing!")
            result="Video is safe for publishing!"
        else:
            # print(f'Obscene content detected! at frame {frame_num}')
            result=f"Obscene content detected @ frame {frame_num}"

        return result

    # result = video_nsfw_detector(fname_u)
    # st.write(result)

  
        result = video_nsfw_detector(fname_u)

            

        

    

# print(result)


