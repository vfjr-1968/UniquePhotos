from PIL import Image
import os

# change this to value of path not the file name
f_path = "/home/vfjr/Pictures/1761.JPG"
# if file extension is JPG do something
im = Image.open(f_path)
exif = im.getexif()
creation_time = exif.get(36867)

print(creation_time)
newname = creation_time + '.JPG'

print(newname)

#os.rename(f_path, newname) 
