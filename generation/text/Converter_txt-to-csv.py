import pandas as pd
import pdb

_MATERIAL_DIR = '../FOLDER_NAME'
_SAVE_DIR = '../FOLDER_NAME'


with open('%s/REFERENCE_FILE_NAME.txt' %(_MATERIAL_DIR)) as f:
    lines = f.readlines()

df = pd.DataFrame(columns = ['ItemNo', 'Sentence1', 'Sentence2', 'Question', 'Answer'])

line_num = 0
idn = 0

while line_num < len(lines):
    # item number
    item_num = lines[line_num].split('# ')[1].split('FILLER ')[1].split(' ')[0]
    item_num = int(item_num) + 100 # to combine fillers with target items
    df.loc[idn, 'ItemNo'] = item_num
    line_num += 1

    # sentence
    sentence = lines[line_num].strip('\n')
    sentence_phrased = sentence.replace('the ', 'the_')
    sentence_phrased = sentence_phrased.replace('The ', 'The_')
    df.loc[idn, 'Sentence1'] = sentence
    df.loc[idn, 'Sentence2'] = sentence_phrased
    line_num += 1

    # question & answer
    question = lines[line_num].strip(' ?').strip('\n')[:-2]
    answer = lines[line_num].strip(' ?').strip('\n')[-1]
    answer = answer.replace('N','no')
    answer = answer.replace('Y', 'yes')
    df.loc[idn, 'Question'] = question
    df.loc[idn, 'Answer'] = answer
    line_num += 1

    idn += 1
# df.to_csv('%s/Fillers.csv' %(_SAVE_DIR), index=False)

df['Length'] = df['Sentence1'].apply(lambda x: len(x.split()))
df_short = df.loc[df['Length'] < 21]
df_short.sort_values(by=['Length'], ascending=False, inplace=True)
df.to_csv('%s/REFERENCE_FILE_NAME-converted.csv' %(_SAVE_DIR), index=False)

