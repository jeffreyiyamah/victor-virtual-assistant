import requests
import io
import os
from dotenv import load_dotenv
import pygame


pygame.init()
pygame.mixer.init()


load_dotenv()
api_key = os.getenv('ELEVEN_LABS_API_KEY')

url = "https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb"
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": api_key
}
data = {
    "text": "Hi, this is Victor, your virtual assistant, specializing in task management and scheduling. How can I assist you today?",
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    audio_stream = io.BytesIO(response.content)

    
    sound = pygame.mixer.Sound(audio_stream)
    
    sound.play()

    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
else:
    print("Failed to get audio. Status code:", response.status_code)
    print("Response:", response.text)
