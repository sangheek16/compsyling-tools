'''
---------------------------------------------------------------------
    This is a basic code for text-to-speech (tts)
    using Google Tranlsate.
    This code does not support large-batch tts.

    Date:           Jul 21 2023 
    Last Updated:   Oct 25 2023
    Author:         Sanghee J Kim

    NOTE:
    Prerequisite:
    - `pip install gTTs` # see: https://pypi.org/project/gTTS/
    
    Variables to change:
    - `_AUDIO_DIR` should be changed
    - `_lang_setup` can be changed
    - `input_sentence` can be changed
    -

    Cautions:
    - do not change this file name to `gtts.py`
      this causes issues
---------------------------------------------------------------------
'''

# https://pypi.org/project/gTTS/

import os
from gtts import gTTS

# set up directory
# _AUDIO_DIR = os.path.join(os.getcwd(), '../FOLDER_NAME_TO_SAVE_AUDIO/')
_AUDIO_DIR = os.path.join(os.getcwd())

# creates a folder if the audio saving folder doesn't exist
# if not os.path.exists(_AUDIO_DIR): 
#     os.makedirs(_AUDIO_DIR)

# setup language
# for other language options see : https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang
_lang_setup = 'en'

# function for generating audio files
def gen_audio(sentence, language, audio_name, audio_dir):
    sentence = sentence.strip()
    audio_name = audio_name.split('.wav')[0]
    audio_output = gTTS(text = sentence, lang = language, slow = False)
    print('> .. Saving %s.mp3' %(audio_name))
    audio_output.save(os.path.join(_AUDIO_DIR, '%s.mp3' %(audio_name)))

'''
--------------------
    Generate audio
--------------------
'''
your_input_sentence = 'Hello, this is a test sentence.'
your_audio_file_name = 'hello'

# -- run code
gen_audio(your_input_sentence, _lang_setup, your_audio_file_name, _AUDIO_DIR)