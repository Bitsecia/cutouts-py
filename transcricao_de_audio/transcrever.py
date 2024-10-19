# instalar biblioteca openai-whisper
# instalar ffmpeg: https://geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
# models: ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo'] 

import whisper
import os

modelo = whisper.load_model("base")
resposta = modelo.transcribe("audio.mp3")

os.system('clear')
print(resposta["text"])
