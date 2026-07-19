import os
import traceback
from instagrapi import Client
from gnews import GNews
from moviepy.editor import *

IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

try:
    print("1. News le raha hun...")
    google_news = GNews(language='hi', country='IN', max_results=1)
    news = google_news.get_news('trending')
    title = news[0]['title']
    print(f"News mili: {title}")

    print("2. Video bana raha hun...")
    # Yahan pehle template check hoga
    img = ImageClip("template.jpg").set_duration(8)

    # Hindi support ke liye font
    txt = TextClip(title, fontsize=55, color='white', size=(1000,1920), method='caption', font='DejaVu-Sans-Bold')
    txt = txt.set_position('center').set_duration(8)

    reel = CompositeVideoClip([img, txt])
    reel.write_videofile("reel.mp4", fps=24, codec="libx264")
    print("Video ban gayi: reel.mp4")

    print("3. Instagram pe upload kar raha hun...")
    cl = Client()
    cl.set_country_code(91)
    cl.set_locale("hi_IN")
    cl.set_timezone_offset(-18000)
    cl.login(IG_USERNAME, IG_PASSWORD)
    print(f"Login ho gaya: {cl.username}")

    media = cl.clip_upload(
        path="reel.mp4",
        caption=f"{title}\n\n#breakingnews #viral #reelsindia #explore"
    )
    print(f"✅ Reel Upload Ho Gayi! Media ID: {media.id}")

except Exception as e:
    print(f"❌ Error: {e}")
    traceback.print_exc()
