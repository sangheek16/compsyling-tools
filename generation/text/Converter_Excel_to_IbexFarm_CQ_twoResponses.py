'''
    -----------------------------------
    Updated:    2021-04-29
    Created:    
    Author :    Sanghee J. Kim
    Source: 
    -----------------------------------

    If using ipython 
    Type $ipython$ in the terminal
    And %paste

'''

'''
-------------------------------------------
    INTRODUCTION
-------------------------------------------

    This is a code to convert material
    in an excel file in a html form
    to fit the Ibex Farm syntax.

    Self-paced reading task
    with comprehenqion question task

'''

'''
-------------------------------------------
    SET UP
-------------------------------------------
'''

import os
import pandas as pd
import numpy as np


'''
-------------------------------------------
    1. Set up directory
-------------------------------------------
'''

_BASE_DIR = ' '     # change directory to the folder where your material is saved

os.chdir(_BASE_DIR)
cwd = os.getcwd()
print(cwd)      # check if you got the right directory


'''
-------------------------------------------
    2. Importing your file 
-------------------------------------------

    I usually work with an .xls before I import
    .xls somehow creates less trouble than .xlsx when you import the file to Python
    You can also use a csv file to import
    Make sure to have your material in a long form

'''

excelFile = os.path.join(_BASE_DIR, 'Kim2021_RCFINAL.xlsx')                                     # insert the file name
df = pd.read_excel(excelFile, 'RCFINAL-main48-filler48-whoCQ', index_col=None, dtype={'ItemNo': str})       # insert the name of the sheet

df.Condition.unique()   # check the types of conditions
df.ItemNo.unique()        # check the number of items
 
df.fillna('', inplace=True)     # converting NaN to empty string

df = df.apply(lambda x: x.str.strip())                  # removes any empty space in the cell except the spacebar
                                                        # use 'apply' for dataframe; use 'map' for column/series                                                        

''' Changing space to _ is optional'''
# for col in df[df.columns[:19]].columns:                 # we will change space to '_' except for the question and answer columns
#   df[col] = df[col].map(lambda x : x.replace(' ', '_'))
''' '''

# with pd.ExcelWriter(excelFile, engine='openpyxl', mode='a') as writer:  
#     df.to_excel(writer, sheet_name='PP & Filler_final', index=False)

'''
-------------------------------------------
    3. Concatenate strings according to the Ibex Farm syntax (Option A)
-------------------------------------------

    The syntax for DashedSentence (with comprehension question):

    [[CONDITION,ITEM], "DashedSentence", {s: ["W1", "W2", "W3", "W4", "W5", "W6", "W7"]} "Question", {q: "question ?", as: ["yes", "no"], hasCorrect: 0 (first option) OR 1 (second option)}],

'''

df.iloc[:,9:] = '"' + df.iloc[:,9:] + '"' # number = ith column where region begins
df['Sentence'] = df.iloc[:,9:].apply(lambda x: ', '.join(x), axis=1) # number = ith column where region begins

df['Sentence'] = df['Sentence'].str.split(', ""', 1).str[0] # method 1
# df['sentence']  = df['sentence'].map(lambda x : x.replace(', ""', '')) # method 2
df['Sentence'][0] # check if the str.split was successful

# df.dyptes
# df.to_csv("final.csv")

df_string = ''      # creating an empty string where we will store the strings we need

for row in df.index:

    df_string += '[[' + '"' + df.loc[row,'Condition'] + '"' + ',' + ' ' + df.loc[row,'ItemNo'] + '], ' +\
    '"DashedSentence", ' + '{s: ' + '[' + df.loc[row,'Sentence'] + ']}, ' +\
    '"Question", ' + '{q: ' + '"' + df.loc[row,'Question'] + '", ' +\
        'as: [[' + '"f","' + df.loc[row,'Choice1'] + '"],["j","' + df.loc[row,'Choice2'] + '"]]}],' + '\n'

print(df_string)

# [["f","yes"],["j","no"]]

'''
-------------------------------------------
    4. Save file
-------------------------------------------
'''

text_file = open("FILE_NAME.txt", "w")     # this will be the file name of the text file
text_file.write(df_string[:-2])                 # remove the last comma and save the file to your directory folder
text_file.close()   


'''
-------------------------------------------
    5. What to do next
-------------------------------------------

    Now check your directory folder;
    You'll see a text file with the file name you designated
    Open that file, copy all the text, and paste it into your Ibex Farm .js file
    Make sure to include this part BEFORE the symbol ]; at the end of the script

'''


''' DOESN'T WORK
separator = ', '
df['sentence'] = np.NaN

for row in df.index:
    col_num = 8
    string_list = []

    while df.iloc[row,col_num] != '':
         string_list.append(str('"' + df.iloc[row,col_num] + '"'))
         col_num += 1

    df.loc[row,'sentence'] = separator.join(string_list)
 '''