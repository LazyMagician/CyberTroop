import re
from home.models import Contact
from django.shortcuts import render,HttpResponse
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from home.models import Video
from tkinter import Image
from django.contrib import messages
from datetime import datetime
import cv2
import math
import numpy as np
# from image_module import commands as image_commands
# from audio import commands as audio_commands
# from video import commands as video_commands
from os import path
import sys
from home.main_pack import main
import PIL
from PIL import Image
import types
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_up(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    # print(request )
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        
        contact.save()
        messages.success(request, 'Your form has been submitted!')
    return render(request,'contact.dhtml')

def main_page(request):
    # return HttpResponse("This is a home page")
    video = Video.objects.all()
#     stegano(request)
#     # return HttpResponse("""<html><script>window.location.replace('')</script></html>""")

# def stegano(request):
    args = ['main.py', 'video' ,'-i', 'D:\cyber_troop\home\output.mp4', '-o' ,'vid_msg.avi', '-m' ,'D:\cyber_troop\home\secret.txt', '-encode', 'shuffle']
    encod_vid = main.main_steg(args)
    return render(request,'main.html',{"video":encod_vid})
    # return render(request,'main.html',{"video":video})

def decode(request):
    print("entered decod")
    args = ['main.py', 'video' ,'-i' ,'D:/cyber_troop/vid_msg.avi', '-k', 'D:\cyber_troop\home\keys', '-decode']
    main.main_steg(args)
    return render(request,'main.html',{"video":"D:/cyber_troop/vid_msg.avi"})
    