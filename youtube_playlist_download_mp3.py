from pytube import YouTube
from pytube import Playlist

import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/watch?v=9TSf2k03HPA&list=PLzBgi-bjxcqIfJBmy8xB53KrcpnwLw2wG")

playlist.video_urls

for url in playlist:
    YouTube(url).streams.filter(only_audio=True).first().download("./cevir/")

folder = "./cevir/"

for file in os.listdir(folder):
    if re.search("mp4",file):
        mp4_path = os.path.join(folder, file)
        mp3_path = os.path.join(folder, os.path.splitext(file)[0]+".mp3")
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)