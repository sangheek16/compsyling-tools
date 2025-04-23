import os
import pandas as pd
import pdb

from gtts import gTTS

# set up directory
_AUDIO_DIR = os.path.join(os.getcwd(), 'audio/audio-check')
_AUDIO_DIR = os.path.join(os.getcwd(), 'audio/filler/input')
_AUDIO_DIR = os.path.join(os.getcwd(), 'audio/practice/input')
_AUDIO_DIR = os.path.join(os.getcwd(), 'audio/target/input')

if not os.path.exists(_AUDIO_DIR):
    os.makedirs(_AUDIO_DIR)

# basic set up for audio files
_lang_setup = 'en'

# supported generation type
_gen_types = ['batch','instance']

# read in material
df = pd.read_excel(os.path.join(os.getcwd(), 'Material.xlsx'), sheet_name='exp2-vwp_filler')

# function for generating audio files
def gen_audio(sentence, language, audio_name, audio_dir):
    audio_output = gTTS(text = sentence, lang = language, slow = False)
    print('> .. Saving %s.mp3' %(audio_name))
    audio_output.save(os.path.join(_AUDIO_DIR, '%s.mp3' %(audio_name)))

'''
--------------------
    Generate audio
--------------------
'''

# by item or by batch
gen_type = str(input("choose one of either -- 'batch', or 'instance'?:  "))

if gen_type == 'batch':
    df.apply(lambda x: gen_audio(x['sentence'], _lang_setup, x['audio'], _AUDIO_DIR), axis=1)

elif gen_type == 'instance':
    sentence_now = str(input("enter sentence you would like to convert to as an audio file:  "))
    audio_name_now = str(input("enter file name you would like to save the audio file as:  "))
    gen_audio(sentence_now, _lang_setup, audio_name_now, _AUDIO_DIR)
    # -- This is a sentence for audio check.
        # -- audio-check-01
    # -- We want to make sure if audio is working!
        # -- audio-check-02
    # -- Please make sure you have the right volume for your audio.
        # -- audio-check-03