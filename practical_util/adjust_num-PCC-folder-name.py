# Purpose is to convert 0-based folder naming system to 1-based

import os

mydir = os.getcwd() # '/home/nykimberly/code/Playgrounds/Data-Science'

folders = os.listdir(mydir)

for folder in folders:
    if folder.startswith('PCC'):
        num_pos = len('PCC_')
        og_num = int(folder[num_pos])
        new_num = og_num + 1
        print("renaming PCC_%d to PCC_%d", og_num, new_num)
        os.rename(folder, 'PCC_' + str(new_num) + folder[num_pos+1:])

print("done")
