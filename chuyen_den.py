import os
import shutil

folder = "D:/code/preprocess"
folder_target = "D:/code/preprocess/data/hand/hand_train"

for file in os.listdir(folder):
    if file.endswith(".jpg"):
        file = os.path.join(folder, file)
        tar = shutil.move(file, folder_target)

