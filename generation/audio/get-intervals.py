import os 
import pandas as pd
import textgrid # https://github.com/kylerbrown/textgrid
import pdb

# set up
choose_input = False

# choose input type
if choose_input:
    _item_types = list(str(input('Is it "target", or "filler"?:  ')))
else:
    _item_types = ['target','filler']


# run code
df = pd.DataFrame()

for itype in _item_types:
    _AUD_DIR = os.path.join(os.getcwd(), 'audio', itype, 'output')
    audio_names = [f for f in os.listdir(_AUD_DIR) if f.endswith('.TextGrid')]

    for aud in audio_names:
        audio_now = os.path.join(_AUD_DIR, aud)
        tgrid = textgrid.read_textgrid(audio_now)
        df_temp = pd.DataFrame(tgrid)
        df_temp['name'] = df_temp['name'].apply(lambda x: x.strip())
        df_temp['name'] = df_temp['name'].apply(lambda x: x.replace('', 'pause') if len(x) == 0 else x)
        df_temp = df_temp.loc[df_temp['tier'] == 'words']
        df_temp = df_temp.drop(['tier'], axis = 1)
        df_temp = df_temp.rename({'name': 'word'}, axis=1)
        df_temp['type'] = itype
        df_temp['audio_name'] = aud.split('.TextGrid')[0]
        df = pd.concat([df, df_temp], ignore_index=True)

# len(df.loc[df['type'] == 'target'].audio_name.unique())
# len(df.loc[df['type'] == 'filler'].audio_name.unique())

# -- Saving target and filler in the same dataframe
_AUD_INFO_DIR = os.path.join(os.getcwd(), 'audio')
df.to_csv('%s/audio_time.csv' %(_AUD_INFO_DIR), index=False)