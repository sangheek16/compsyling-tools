import pandas as pd
import re
import pdb 

_DIR_MATERIAL = ' '

with open('%s/REFERENCE_FILE_NAME.txt' %(_DIR_MATERIAL)) as f:
    lines = f.readlines()[0]

m = re.split('\d+. ',lines)

material = dict()
for i in range(1, len(m)):
    sentences = m[i].split('. ')
    material[i] = dict()
    for j in range(0,6):
        material[i]['condition_'+str(j+1)] = m[i].strip().split('. ')[j].strip('.')+'.'
        # pdb.set_trace()

material = pd.DataFrame(material).T.reset_index().rename({'index':'item_num'}, axis=1)
material = pd.wide_to_long(material, "condition_", i="item_num", j="condition").rename({'condition_':'sentence'}, axis=1).reset_index()
material = material.sort_values(by=['item_num']).reset_index().drop(['index'],axis=1)

material.to_csv('%s/REFERENCE_FILE_NAME-converted.csv' %(_DIR_MATERIAL), index=False)