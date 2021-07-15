from pathlib import WindowsPath
from django.shortcuts import render
from .models import ImageTarget, Video

from .web_demo import WebDemo
import json
from os.path import exists

import cv2
import PIL
import numpy as np
from moviepy.editor import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.POST:

        title = request.POST["title"]
        video = request.FILES["videofile"]

        vids = Video(title = title, videofile = video)
        vids.save()

        vidobj = cv2.VideoCapture(vids.videofile.path)
        frame_list = []

        while True:
            ret, frame = vidobj.read() # 프레임 정보, 프레임
            frame_list.append(frame)

            if not ret:
                break
        
        frame_list = frame_list[:-1]
        videos = {'ims':frame_list, 'coordinates':(168, 109, 144, 283)}
        config_path = 'erAIser/config_web.json'
        config = json.load(open(config_path))
        inpainted, _, _ = WebDemo(videos=videos, cfg=config)

        for i, im in enumerate(frame_list):
            cv2.imwrite('media/src_img/{}.png'.format(i), im)  # src_img 폴더 만들어두고 작업해야 write 가능
        
        ims_list = ['media/src_img/{}.png'.format(i) for i in range(len(frame_list))]
        clip = ImageSequenceClip(ims_list, fps=50)
        clip.write_videofile("media/rst/video.mp4", fps=50)
        vid_path = "/media/rst/video.mp4"

        if vidobj.isOpened():
            vidobj.release()


        context = {
            'vids': vids,
            'frame_length': len(frame_list),
            'vid_path': vid_path
        }

        return render(request, 'result.html', context)