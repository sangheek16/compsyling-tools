'''
    -----------------------------------
    Created:    2020-11-05
    Updated:    
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
    with acceptability judgment task

'''

'''
-------------------------------------------
    SET UP
-------------------------------------------
'''

import os
import pandas as pd


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

excelFile = os.path.join(_BASE_DIR, 'Kim2020_material_Exp3_v0.1.xlsx')                                     # insert the file name
df = pd.read_excel(excelFile, 'Exp3_ORC_Full', index_col=None, dtype={'condition': str, 'item': str})       # insert the name of the sheet

df.condition.unique()   # check the types of conditions
df.item.unique()        # check the number of items

# df.drop(df.columns[[-1, -2]], axis=1, inplace=True)     # this line can be commented out if your df contains only the columns you want to use 
 
df.fillna('', inplace=True)     # converting NaN to empty string

# df_obj = df.select_dtypes(['object'])
# df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())                                                                   
df = df.apply(lambda x: x.str.strip())                  # removes any empty space in the cell except the spacebar
                                                        # use 'apply' for dataframe; use 'map' for column/series                                                        

'''
-------------------------------------------
    3. Concatenate strings according to the Ibex Farm syntax
-------------------------------------------

    The syntax for DashedAcceptabilityJudgment (an example with 7 regions):

    [[CONDITION,ITEM], "DashedAcceptabilityJudgment", {s: ["W1", "W2", "W3", "W4", "W5", "W6", "W7"]}],

    We will replace the CONDITION, ITEM, W1, ... , W7 with the words/numbers from our excel file.

    Author Note:
    I already had a period in my final word region; I won't be adding a period in the script below.
    All the sentences I used had either 9 or 10 region;
    My code below reflects this

'''

df_string = ''      # creating an empty string where we will store the strings we need


''' Ten Regions '''

## Option 1: Ten regions total

for row in df.index:
    
    # if the sentence has 8 regions

    if df.loc[row,'w9'] == '':     
        df_string += '[[' + '"' + df.loc[row,'condition'] + '"' + ',' + ' ' + df.loc[row,'item'] + ']' + ',' + '"' +\
        'DashedAcceptabilityJudgment' + '"' + ',' + ' ' + '{' + 's' + ':' + ' ' + '[' +\
        '"' + df.loc[row,'w1'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w2'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w3'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w4'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w5'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w6'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w7'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w8'] + '"' +\
        ']' + '}' + ']' + ',' + '\n'

    # if the sentence has 9 regions

    elif df.loc[row,'w10'] == '':     
        df_string += '[[' + '"' + df.loc[row,'condition'] + '"' + ',' + ' ' + df.loc[row,'item'] + ']' + ',' + '"' +\
        'DashedAcceptabilityJudgment' + '"' + ',' + ' ' + '{' + 's' + ':' + ' ' + '[' +\
        '"' + df.loc[row,'w1'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w2'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w3'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w4'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w5'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w6'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w7'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w8'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w9'] + '"' +\
        ']' + '}' + ']' + ',' + '\n'

    # if the sentence has 10 regions

    else:                           
        df_string += '[[' + '"' + df.loc[row,'condition'] + '"' + ',' + ' ' + df.loc[row,'item'] + ']' + ',' + '"' +\
        'DashedAcceptabilityJudgment' + '"' + ',' + ' ' + '{' + 's' + ':' + ' ' + '[' +\
        '"' + df.loc[row,'w1'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w2'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w3'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w4'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w5'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w6'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w7'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w8'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w9'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w10'] + '"' +\
        ']' + '}' + ']' + ',' + '\n'


''' Nine Regions '''

## Option 2: Nine regions total

for row in df.index:

    # if the sentence has 8 regions

    if df.loc[row,'w9'] == '':     
        df_string += '[[' + '"' + df.loc[row,'condition'] + '"' + ',' + ' ' + df.loc[row,'item'] + ']' + ',' + '"' +\
        'DashedAcceptabilityJudgment' + '"' + ',' + ' ' + '{' + 's' + ':' + ' ' + '[' +\
        '"' + df.loc[row,'w1'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w2'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w3'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w4'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w5'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w6'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w7'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w8'] + '"' +\
        ']' + '}' + ']' + ',' + '\n'

    # if the sentence has 9 regions

    else:     
        df_string += '[[' + '"' + df.loc[row,'condition'] + '"' + ',' + ' ' + df.loc[row,'item'] + ']' + ',' + '"' +\
        'DashedAcceptabilityJudgment' + '"' + ',' + ' ' + '{' + 's' + ':' + ' ' + '[' +\
        '"' + df.loc[row,'w1'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w2'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w3'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w4'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w5'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w6'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w7'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w8'] + '"' + ',' + ' ' +\
        '"' + df.loc[row,'w9'] + '"' +\
        ']' + '}' + ']' + ',' + '\n'


print(df_string)


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