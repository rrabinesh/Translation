# import os
# from pydub import AudioSegment
# from gtts import gTTS
# from pydub.playback import play
# from googletrans import Translator

# def text_to_speech(text, lang):
#     translator = Translator()
#     translated_text = translator.translate(text, src='en', dest=lang).text
    
#     tts = gTTS(text=translated_text, lang=lang, slow=False)
#     tts.save("output.mp3")
    
#     return AudioSegment.from_mp3("output.mp3")

# # English text to be converted
# english_text = "Hello, What is your name?"

# # Language code for Tamil
# language = 'ta'

# audio = text_to_speech(english_text, language)

# play(audio)

import os
from gtts import gTTS
from playsound import playsound  # For playing the audio
from googletrans import Translator
from fastapi import FastAPI
from datetime import datetime
from fastapi.staticfiles import StaticFiles

app = FastAPI()

def text_to_speech(text):
    if not os.path.exists("output_audios"):
        os.makedirs("output_audios")
    lang = 'ta'
    tts = gTTS(text=text, lang=lang, slow=False)
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{current_time}.mp3"
    file_path = os.path.join("output_audios", file_name)
    tts.save(file_path)  # Save the generated audio with timestamped filename
    return file_path

# English text to be converted
# english_text = "Hello, What is your name?"

# Language code for Tamil
# target_language = 'ta'

translator = Translator()
# translated_text = translator.translate(english_text, src='en', dest=target_language).text

# audio_file = text_to_speech(translated_text)
# playsound(audio_file)  # Play the generated audio
app.mount("/output_audios", StaticFiles(directory="output_audios"), name="output_audios")
@app.get("/audio_translate/")
def convertt(english_text: str,
             target_language: str):
    translated_text = translator.translate(english_text, src='en', dest=target_language).text
    audio_file = text_to_speech(translated_text)
    return audio_file