'''
--------------------------------------------------
    This code produces images using DALL-E
    Author: Sanghee J. Kim
    Date: Mar 26, 2023

    NOTE: Make sure to change the codes that has 
          'CHANGE THIS' tag in the line
--------------------------------------------------
'''


import pandas as pd
import numpy as np
import os
import datetime, time
import requests
import openai

'''
-------------------------
    Base set up
-------------------------
'''

# -- Set up OpenAI API key
# get OpenAI API key: https://beta.openai.com/account/api-keys
openai.api_key = "KEY" # CHANGE THIS

# -- Set up path and read in files
# read in the list of nouns (this can be done in different ways) # CHANGE THIS
df = pd.read_excel(os.path.join(os.getcwd(), 'material.xlsx'), sheet_name='exp2-vwp') # CHANGE THIS
noun_list = list()
noun_list.extend(df['image1'].tolist()) # CHANGE THIS
noun_list.extend(df['image2'].tolist()) # CHANGE THIS
noun_list.extend(df['image3'].tolist()) # CHANGE THIS
noun_list.extend(df['image4'].tolist()) # CHANGE THIS
noun_list = sorted(list(set(noun_list)))

# set directory where you will save the image
_IMG_DIR = os.path.join(os.getcwd(), 'FOLDER_NAME') # CHANGE THIS
if not os.path.exists(_IMG_DIR):
    os.makedirs(_IMG_DIR)

# set up number of images to generate
_gen_num = 4 # CHANGE THIS

'''
-------------------------
    Helper Functions
-------------------------
'''

# generating url for the images
def generate_images(input_prompt, max_generate_num):
    output_dict = dict()
    response = openai.Image.create(
        prompt = input_prompt,
        n = max_generate_num,
        size = "256x256" # set up image resolution # "1024x1024" # CHANGE THIS
    )
    for n in range(0, max_generate_num):
        output_dict[n] = response['data'][n]['url']
    return output_dict

'''
-------------------------
    Get Images
-------------------------
'''

# -- get noun list
batch_list = noun_list 
# batch_list = ['cats'] # you can use this to see if the code works

# -- generate and images
noun_num = 0
for noun in batch_list:
    start_time = datetime.datetime.now()
    prompt = 'drawing of two %s in black and white thick pen line drawing digital art with white background' %(noun)
    print('> Generating %s picture(s) of "%s" (%s/%s) ... ' %(_gen_num, noun, noun_num+1, len(batch_list)))
    url_dict = generate_images(prompt, _gen_num)
    for k, v in url_dict.items():
        query_num = k
        img = requests.get(v)
        print('> Saving image %s/%s of "%s" ...' %(query_num+1, _gen_num, noun))
        open('%s/%s-%s.png' %(_IMG_DIR, noun, query_num+1), 'wb').write(img.content)

    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time).total_seconds() * 1
    print('Processing time for generating and saving images of "%s": %d seconds' %(noun, execution_time))

    noun_num += 1
    time.sleep(3) # time lag not to exceed 50 images / min