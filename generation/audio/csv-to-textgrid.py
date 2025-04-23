import pandas as pd
import os
from praatio import textgrid
import pdb


'''
----------------------------------------------------------------
    Prep: Base information

    - material and this code are in the same directory
    - aux files and textgrids are in a lower directory ('audio')
----------------------------------------------------------------
'''
# set up target tier
_tier_names = ['sentence','words'] # possible tiers

# set up directory
_AUDIO_DIR = os.path.join(os.getcwd(), 'audio/filler')
_MATERIAL_DIR = os.path.join(os.getcwd())


'''
----------------------------------------------------------------
    Prep: Assign file specifications
----------------------------------------------------------------
'''
# audio extension
audio_ext = '.mp3'

# assign current target tier
target_name = _tier_names[0]

# data file names
my_data = 'Material.xlsx'
my_sheet = 'exp2-vwp_filler'

'''
----------------------------------------------------------------
    Prep: Read in files
----------------------------------------------------------------
'''
# read in material and save it to a new variable that includes
    # (1) name of the audio file, and 
    # (2) the text that should be included in the textgrid
df = pd.read_excel(os.path.join(_MATERIAL_DIR, my_data), \
    sheet_name = my_sheet)
df[target_name] = df[target_name].map(lambda x: x.strip())
target_pair = dict(zip(df['audio'], df[target_name]))

# read in text grid files
file_list = [f for f in os.listdir(_AUDIO_DIR) if f.endswith('.TextGrid')]
audio_list = [f for f in os.listdir(_AUDIO_DIR) if f.endswith(audio_ext)]

# stop if the number of textgrids and audio files does not match
fl_elm = sorted([x.split('.TextGrid')[0] for x in file_list])
al_elm = sorted([x.split('.mp3')[0] for x in audio_list])

if fl_elm != al_elm:
    raise ValueError('The audio file and textgrid do not match!')

'''
----------------------------------------------------------------
    Main task
----------------------------------------------------------------
'''
# read textgrids and map target sentences/words
for f_name in file_list:

    # NOTE: tier needs to be 'selected' and then saved
    # otherwise there will be an out of range index error
    tg = textgrid.openTextgrid(os.path.join(_AUDIO_DIR, f_name), False)

    # get duration of the audio input
    start = tg.minTimestamp
    end = tg.maxTimestamp

    # map target sentence onto the target audio
    target_input = target_pair[f_name.split('.TextGrid')[0]]

    targetTier = tg.tierDict[target_name]
    targetTier.insertEntry((start, end, target_input), \
        collisionMode = 'replace')
    tg.replaceTier(target_name, targetTier)
    # print(targetTier.entryList)

    tg.save(fn = os.path.join(_AUDIO_DIR, f_name), \
        format = 'short_textgrid', \
        includeBlankSpaces = False)

    print('> ... Converted %s' %(f_name))
