import os
import re
import itertools
import shutil

print("Starting SSD5 MIDI sorting.")

# 1. Create directories for different groove categories
for filenameA in os.listdir(os.getcwd()):
    fileCurrent = filenameA.rstrip(".mid")
    fileCurrent = re.sub(r'\d+$', "", fileCurrent)
    print(fileCurrent)
    print("Creating directory:")
    if not os.path.exists(fileCurrent):
        try:
            os.mkdir(fileCurrent+".prt")
        except:
            continue

# 2. Move all category files to matching directories
for filenameB in os.listdir(os.getcwd()):
    if os.path.isfile(filenameB) == False:
        print("not file!")
        continue
    fileCurrent = filenameB.rstrip(".mid")
    fileCurrent = re.sub(r'\d+$', "", fileCurrent)
    print(fileCurrent)
    if os.path.exists(fileCurrent+".prt"):
        try: 
            shutil.move(filenameB, fileCurrent+".prt")
        except:
            continue
print("Script finished.")
    
