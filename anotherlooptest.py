#importing os module
import os, hashlib

#providing the path of the directory
#r = raw string literal
#dirloc = r"/home/vfjr/Pictures/UniquePhotos" 
dirloc = r"/home/vfjr/Documents/Scripts/Python"
#calling scandir() function
for file in os.scandir(dirloc):
    #if (file.path.endswith(".JPG") or file.path.endswith(".py")) and file.is_file():
    filename = file.path
    BLOCK_SIZE = 65536 # The size of each read from the file
file_hash = hashlib.sha256() # Create the hash object
with open(filename, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file
        #print(file.path)
        print(filename)
        print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash