import os
import shutil

source = os.getcwd()

for f in os.listdir(source):

    if f.startswith("ML_"):
        print("folder starts with ML_")
        prefix = "ML"
        dest = os.path.join(source, prefix)
        new_f = f[len(prefix)+1:]

    elif f.startswith("PCC_"):
        print("folder starts with PCC_")
        prefix = "PCC"
        dest = os.path.join(source, prefix)
        new_f = f[len(prefix)+1:]

    else:
        print("don't need to move this folder")
        continue

    print("processing folders")
    os.rename(f, new_f)
    shutil.move(new_f, dest)

print("restructuring completed.")
