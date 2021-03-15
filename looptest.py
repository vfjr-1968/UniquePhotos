import os

folderpath='/home/vfjr/Pictures/UniquePhotos'
for root, dirs, files in os.walk(folderpath):
    for file in files:
        #if file == myfile:
        print(file)
        print(os.name)