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

dashboard_mesaj = '''

    __     __      _______    _            _____                      _                 _
    \ \   / /     |__   __|  | |          |  __ \                    | |               | |
     \ \_/ /__  _   _| |_   _| |__   ___  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __
      \   / _ \| | | | | | | | '_ \ / _ \ | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
       | | (_) | |_| | | |_| | |_) |  __/ | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
       |_|\___/ \__,_|_|\__,_|_.__/ \___| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|


                     YouTube Mp3/Mp4 Downloader | Twitter: @k4juxi

                                Developer: Veysel BAY

'''
print(dashboard_mesaj)

hedef_klasor = input("İndirilecek klasörün yolu:  \n\nExample:/home/developer/Desktop/musics/\n\n                         :")


sarki = input("Şarkı adını giriniz: ")
url = "https://www.youtube.com/results?search_query="+sarki
sayfa = requests.get(url)
parset = BeautifulSoup(sayfa.content, 'html.parser')
sarkilar = []
linkler = []
for i in range(8):
    for a in parset.find_all('a', title=True,href=True):
        if a['href'][:2] == "/w":
            sarkilar.append(a['title'])
            linkler.append(a['href'])

for i in range(8):
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
        bul=dosya
    os.rename(hedef_klasor+bul,hedef_klasor+"video.mp4")
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
