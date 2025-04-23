import os 
import pandas as pd
import pdb

# set directory
_MATERIAL_DIR = os.getcwd()
_AUDIO_INFO_DIR = os.path.join(os.getcwd(), 'audio')

# helper functions
def add_regionNo(group): # assigns region number
    group['region_no'] = range(len(group))
    return group

def handle_pause(group): # removes incorrect 'pause' labels and adds length to the previous region
    # if group.condition.str.contains('restr_').all():
    imgs = [group.iloc[0].image1.split('.')[0], group.iloc[0].image2.split('.')[0]]
    final_idx = len(group)-1
    pause_added = []
    for idx, row in enumerate(group.itertuples()):
        if row.word == 'pause' and idx != 0 and idx != final_idx:
            if group.condition.str.contains('appos_').all():
                if group.loc[row.Index-1, 'word'] in imgs:
                    continue
            pause_added.append(idx)
            group.loc[row.Index-1, 'stop'] = group.loc[row.Index, 'stop']
    group['pause_added'] = [1 if i+1 in pause_added else 0 for i in range(len(group))]
    group = group[~group.region_no.isin(pause_added)]
    group = add_regionNo(group)
    return group


# read in df
df = pd.read_excel('%s/Material.xlsx' %(_MATERIAL_DIR), sheet_name = 'exp2-vwp_all', converters={'item': str})
df.rename({'audio': 'audio_name'}, axis=1, inplace=True)
df.drop(['list', 'block', 'question', 'question_pcibex'], axis=1, inplace=True)
df_aux = pd.read_csv('%s/audio_time.csv' %(_AUDIO_INFO_DIR))
df_aux['audio_name'] = df_aux['audio_name'] + '.wav'

# combine data frames
combined_df = pd.merge(df, df_aux, on=['type', 'audio_name'], how='right')

# add region number
combined_df = combined_df.groupby(['item', 'condition', 'latin']).apply(add_regionNo)

# apply the function to the dataframe and create a new 'position' column
combined_df = combined_df.groupby(['item', 'condition', 'latin']).apply(handle_pause).reset_index(drop=True)

# save the audio info mapped dataframe
combined_df.to_csv('%s/audio_time_mapped.csv' %(_AUDIO_INFO_DIR), index=False)