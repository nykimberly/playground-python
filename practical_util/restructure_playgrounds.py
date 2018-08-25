########## Background ##########
# I named a bunch of directors as "Playground_<language>"
# I wanted to rename them because navigating to any one of them 
# required too many keystrokes
# i.e. P+TAB = "Playground_", then B+TAB = "Playground_Bash"

########## Proposal ##########
# I hang around in my playground a lot, so
# I figured I'd just put all my sandboxes in one Playground umbrella
# then rename my sandboxes to just their <language> value.

########## Implementation ##########
# Part I: Move all my current playgrounds to an umbrella dir Playgrounds
# Part II: Remove "Playground" from name of each file

# Note: Part II can be done w/ or w/o Part I due to the "If" cond.

import os
import shutil

source = '/home/nykimberly/code'
# alternatively, if in current working directory, assign to os.getcwd()
dest = '/home/nykimberly/code/Playgrounds'

files = os.listdir(source)

for f in files:
	if (f.startswith("Playground")):
		os.rename(f, f[11:])
		shutil.move(f, dest)
