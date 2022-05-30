from home.models import Contact
from django.shortcuts import render,HttpResponse
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from home.models import Video
from tkinter import Image
from django.contrib import messages
import time
import os
from datetime import datetime
import cv2
import math
import numpy as np
import PIL
from PIL import Image
import types
from home.modules.helo import helo_check  
import requests

# Create your views here.
def helo(request):
    return helo_check(request)
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
    return render(request,'main.html',{"video":video})

    
def video_trim(request):
    start = int(input("Enter the start time: "))
    end =  int(input("Enter the end time: "))
    print(start,end)
    ffmpeg_extract_subclip("home\Attach Baya Ka Bavarla_Full-HD.mp4", start, end, targetname="home\_test_vid.mp4")
    data = time_frame(request) 
    # return render(request,)
    return HttpResponse("""<html><script>window.location.replace('/')</script></html>""")
    # clip = VideoFileClip('test.mp4')
    # clip = clip.subclip(0,15)
    # clip = clip.cutout(3,10)
    # clip.ipython_display(width=360)


def time_frame(request):
    count = 0
    cap = cv2.VideoCapture('home\_test_vid.mp4')
    time = int(input("Enter the time frame in seconds"))
    cap.set(cv2.CAP_PROP_POS_MSEC,time*1000)
    success,image = cap.read()
    print(success)
    # creating a folder if it doesnt exits
    if not os.path.exists('./frames'):
        os.mkdir('./frames')
    if success:
        cv2.imwrite('./frames/'+str(time)+'.png',image)
    cap.release()
    cv2.destroyAllWindows()
    img_path = "D:/cyber_troop/frames/24.png"
    img = encode(request,img_path,'abc123')
    cv2.imwrite('D:\cyber_troop\home\encod_img.png', img)
    decode(request,'D:\cyber_troop\home\encod_img.png')
    return ("Done!")
    # return HttpResponse("""<html><script>window.location.replace('/')</script></html>""")

def to_bin(request,data):
    if isinstance(data,str):
        print(' '.join([format(ord(i),'08b')for i in data]))
        return ''.join([format(ord(i),'08b')for i in data])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


# function to encode the data into the image
def encode(request,img_name,data):
    print("enter the encode")
    img = cv2.imread(img_name)
    ind = 0
    data += '===='
    bin_data = to_bin(request,data)
    print(bin_data)
    data_len = len(bin_data)
    # the range will be updated with a random function from the list 
    for value in range(0,len(img)):
        for pix in img[value]:
            
    # encrypt char ascii 1st bit and last bit per row    
    # for value in range(0,len(img)):
        # pix = img[0]
        # last_bit_enc(pix)
        # pix = img[-1] 
        # last_bit_enc(pix)    

    # encrypt char ascii 1st bit and last bit per row   
    # incr = randomint change it each month  
    # for value in range(0,len(img)):
    #   for pix in range(0,len(value),incr):
        # last_bit_enc(pix)


            r,g,b = to_bin(request,pix)
            # print(r," ",g," ",b)
            if ind < data_len:
                pix[0] = int(r[:-1] + bin_data[ind],2)
                ind += 1
            if ind < data_len:
                pix[1] = int(g[:-1] + bin_data[ind],2)
                ind += 1    
            if ind < data_len:
                pix[2] = int(b[:-1] + bin_data[ind],2)
                ind += 1
            print(to_bin(request,pix[0])[-1]," ",to_bin(request,pix[1])[-1]," ",to_bin(request,pix[2])[-1],"ind:",ind,"datalen:",data_len)
            if ind >= data_len:
                break
        if ind >= data_len:
            break
    return img


# function to decode the data in the image
def decode(request,img_name):
    img = cv2.imread(img_name)
    bin_data = ''                       
    for row in range(0,len(img)):
        for pix in img[row]:
            r,g,b = to_bin(request,pix)
            # print(r," ",g," ",b)
            bin_data += r[-1] 
            bin_data += g[-1] 
            bin_data += b[-1]
    # print(bin_data)
    all_bytes = [bin_data[i:i+8]for i in range(0,len(bin_data),8)]       #splitting the binary string to bytes 
    # print(all_bytes)
    dec_data = ""
    # convert each byte to character
    for i in all_bytes:
        dec_data += chr(int(i,2))
        # print(dec_data)
        if dec_data[-4:] == "====":
            break
    print(dec_data[:-4])
    # print(dec_data[:-4])
# img_path = "D:/cyber_troop/frames/24.png"
# img = encode(img_path,'abc123')
# # print(img)

# def stegano(request):