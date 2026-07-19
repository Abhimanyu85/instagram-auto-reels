import os
from instagrapi import Client
from gnews import GNews
from moviepy.editor import *

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

google_news = GNews(language='hi', country='IN', max_results=1)
news = google_news.get_news('trending')
title = news[0]['title']

img = ImageClip("template.jpg").set_duration(7)
txt = TextClip(title, fontsize=70, color='white', size=(1080,1920), method='caption')
txt = txt.set_position('center').set_duration(7)
reel = CompositeVideoClip([img, txt])
reel.write_videofile("reel.mp4", fps=24)

cl = Client()
cl.login(IG_USERNAME, IG_PASSWORD)
cl.clip_upload(path="reel.mp4", caption=f"{title}\n\n#news #trending")

print("Auto Reel Upload Ho Gayi!")
