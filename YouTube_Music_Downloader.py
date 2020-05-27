#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pytube import *
import os
import subprocess
import ffmpeg
import re
import time
hedef_klasor = "/home/vysl/Desktop/müzikler/"

sarki = input("Şarkı adını giriniz: ")
url = "https://www.youtube.com/results?search_query="+sarki
sayfa = requests.get(url)
parset = BeautifulSoup(sayfa.content, 'html.parser')
sarkilar = []
linkler = []
for i in range(20):
    for a in parset.find_all('a', title=True,href=True):
        if a['href'][:2] == "/w":
            sarkilar.append(a['title'])
            linkler.append(a['href'])

for i in range(20):
    print(i+1,"-",sarkilar[i])
secim = int(input("İndirilecek Müziği seçin: "))
os.system('cls' if os.name == 'nt' else 'clear')
sec = input("Video İçin  1\n\nMp3 İçin    2\n\n           :")
os.system('cls' if os.name == 'nt' else 'clear')
if sec == "1":
    link="https://www.youtube.com"+linkler[secim-1]
    y = YouTube(link)
    t = y.streams.first()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("İNDİRİLİYOR...")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    t.download(hedef_klasor)
    print("TAMAMLANDI...")
if sec == "2":
    link="https://www.youtube.com"+linkler[secim-1]
    y = YouTube(link)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("İNDİRİLİYOR...")
    t = y.streams.first()
    t.download(hedef_klasor)

    for dosya in [n for n in os.listdir(hedef_klasor) if re.search('mp4',n)]:
        buldum=dosya
    os.rename(hedef_klasor+buldum,hedef_klasor+"video.mp4")
    #MP3'E çevirme
    mp4 = ("%s.mp4" %(hedef_klasor+'video'))
    mp3 = ("%s.mp3" %(hedef_klasor+'video2'))
    ffmpeg = ('ffmpeg -i %s ' %(mp4+" "+mp3))
    subprocess.call(ffmpeg, shell=True)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.rename(hedef_klasor+"video2.mp3",hedef_klasor+sarkilar[secim-1]+".mp3")
    sil=('rm '+hedef_klasor+'video.mp4')
    subprocess.call(sil, shell=True)
    print("\nTAMAMLANDI\n")
