import json
import random
import datetime
import openai
from gtts import gTTS
from moviepy.editor import *

# Load topics
with open("topics.json", "r") as f:
    topics = json.load(f)

# Pick today's topic
today = datetime.date.today()
topic = topics[today.day % len(topics)]

# Generate script using ChatGPT
openai.api_key = "YOUR_OPENAI_API_KEY"

prompt = f"Write a YouTube video script about {topic} in 300 words, engaging and informative."
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=600
)
script = response.choices[0].text.strip()

# Save script
with open("script.txt", "w") as f:
    f.write(script)

# Convert script to audio
tts = gTTS(script)
tts.save("voice.mp3")

# Create video (simple background)
clip = TextClip(script, fontsize=40, color='white', bg_color='black', size=(1080,1920))
clip = clip.set_duration(60)  # 1 min video
audio = AudioFileClip("voice.mp3")
final = clip.set_audio(audio)

final.write_videofile("video.mp4", fps=24)

print("✅ Video created successfully: video.mp4")
