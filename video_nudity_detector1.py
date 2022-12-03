
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
import os.path
ffmpeg_path_os = os.path.join('ffmpeg','bin')
ffmpeg_path_pthlib = Path('ffmpeg') / 'bin'

print(ffmpeg_path_os)
print(ffmpeg_path_pthlib)
model_path = Path('model_mobilenet')/ 'saved_model.h5'
print(model_path)
skvideo.setFFmpegPath(ffmpeg_path_os)
import skvideo.io
