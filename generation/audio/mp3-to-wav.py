import os
from pydub import AudioSegment # $ brew install ffmpeg
import sys

# assign item type
file_type = str(input("enter file type -- 'target', 'filler', 'practice', 'audio_check':  "))

# set directory 

if file_type in ['target','filler','practice']:
    _DIR_AUDIO_INPUT = os.path.join(os.getcwd(), 'audio', file_type, 'input/')
    _DIR_AUDIO_OUTPUT = os.path.join(os.getcwd(), 'audio', file_type, 'input/')
else:
    _DIR_AUDIO_INPUT = os.path.join(os.getcwd(), 'audio', file_type)
    _DIR_AUDIO_OUTPUT = os.path.join(os.getcwd(), 'audio', file_type)

if not os.path.exists(_DIR_AUDIO_OUTPUT):
    os.makedirs(_DIR_AUDIO_OUTPUT)

# get files
audio_input = [f for f in os.listdir(_DIR_AUDIO_INPUT) if f.endswith('.mp3')]

# convert mp3 to wav
for aud in audio_input:
    sound = AudioSegment.from_mp3(os.path.join(_DIR_AUDIO_INPUT, aud))
    sound.export(os.path.join(_DIR_AUDIO_OUTPUT, aud.split('.mp3')[0] + '.wav'), format = "wav")


# --- Basic example

# from pydub import AudioSegment
# sound = AudioSegment.from_mp3("myfile.mp3")
# sound.export("myfile.wav", format="wav")

