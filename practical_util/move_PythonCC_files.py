import os
import shutil

subject = "PythonCC"

source = os.getcwd()
dest = os.path.join(source, "PythonCC_DataVisualization")

files = os.listdir(source)

for f in files:
    if (f.startswith(subject)):
        new_f = f[len(subject + "_"):]
        os.rename(f, new_f)
        shutil.move(new_f, dest)
