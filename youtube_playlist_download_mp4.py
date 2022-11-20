from pytube import YouTube
from pytube import Playlist


playlist = Playlist("https://www.youtube.com/watch?v=9TSf2k03HPA&list=PLzBgi-bjxcqIfJBmy8xB53KrcpnwLw2wG")

playlist.video_urls

for url in playlist:
    YouTube(url).streams.filter(only_audio=True).first().download("./converted/")