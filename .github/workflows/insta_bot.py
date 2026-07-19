import os
import random
from instagrapi import Client
from gnews import GNews
from moviepy.editor import *
import requests

# 1. SECRETS LOADING
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
GNEWS_KEY = os.getenv("GNEWS_KEY")

# 2. REEL CATEGORIES
CATEGORIES = {
    "humore": ["funny", "comedy", "meme"],
    "love": ["love", "couple", "romantic"],
    "party": ["party", "celebration", "festival"],
    "dancing": ["dance", "dancing", "choreography"]
}

CAPTIONS = {
    "humore": "Hasi rok nahi paoge 😂 #funny #comedy #viralreels",
    "love": "Dil se dil tak ❤️ #love #couple #romantic",
    "party": "Party mode ON 🥳 #party #vibes #dance",
    "dancing": "Dance karne ka mann kar gaya? 🕺 #dance #reels #viral"
}

HASHTAGS = "#viralreels #trending #instagram #reelsinstagram #explorepage"

# 3. VIDEO DOWNLOAD - GNEWS SE
def get_video(category):
    keyword = random.choice(CATEGORIES[category])
    google_news = GNews(language='en', country='US', max_results=3)
    news = google_news.get_news(keyword)
    
    if news:
        video_url = news[0]['url'] # Yahan tum royalty-free video ka link daal sakte ho
        # Abhi demo ke liye hum local video use karenge
        return "sample.mp4" 
    return "sample.mp4"

# 4. VIDEO EDIT KARNA
def edit_video(input_path, category):
    clip = VideoFileClip(input_path).subclip(0, 15) # 15 sec ki reel
    clip = clip.resize(height=1080)
    
    # Text add karna
    txt = TextClip(f"{category.upper()} VIBES", fontsize=70, color='white', font='Arial-Bold')
    txt = txt.set_position('center').set_duration(3)
    
    final = CompositeVideoClip([clip, txt])
    output_path = f"final_reel_{category}.mp4"
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path

# 5. INSTAGRAM PE UPLOAD
def upload_reel(video_path, category):
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    
    caption = CAPTIONS[category] + "\n\n" + HASHTAGS
    cl.clip_upload(video_path, caption)
    print(f"Uploaded {category} reel successfully!")

# 6. MAIN FUNCTION
def main():
    category = random.choice(list(CATEGORIES.keys()))
    print(f"Selected Category: {category}")
    
    video = get_video(category)
    final_video = edit_video(video, category)
    upload_reel(final_video, category)

if __name__ == "__main__":
    main()
