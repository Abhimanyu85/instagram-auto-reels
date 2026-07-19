import os
import time
from instagrapi import Client
from gnews import GNews
from moviepy.editor import *

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

try:
    # 1. Khud News lega
    print("News le raha hun...")
    google_news = GNews(language='hi', country='IN', max_results=1)
    news = google_news.get_news('trending')
    title = news[0]['title']
    print(f"News mili: {title}")

    # 2. Khud Video banayega - template.jpg chahiye
    print("Video bana raha hun...")
    img = ImageClip("template.jpg").set_duration(8)
    txt = TextClip(title, fontsize=65, color='white', size=(1000,1920), method='caption', font='Arial-Bold')
    txt = txt.set_position('center').set_duration(8)
    reel = CompositeVideoClip([img, txt])

    # 8 sec ka audio add karo agar audio.mp3 hai to
    # reel = reel.set_audio(AudioFileClip("audio.mp3").subclip(0,8))

    reel.write_videofile("reel.mp4", fps=24, codec="libx264")

    # 3. Khud Upload karega - Device setting ke sath
    print("Instagram pe upload kar raha hun...")
    cl = Client()

    cl.set_country_code(91) # India
    cl.set_locale("hi_IN") # Hindi
    cl.set_timezone_offset(-18000) # IST
    cl.login(IG_USERNAME, IG_PASSWORD)
    cl.delay_range = [2, 5] # Human jaisa delay

    media = cl.clip_upload(
        path="reel.mp4",
        caption=f"{title}\n\n📰 Breaking News\n\n#news #india #trendingreels #vibehub"
    )
    print(f"✅ Reel Upload Ho Gayi! Media ID: {media.id}")

except Exception as e:
    print(f"❌ Error: {e}")
