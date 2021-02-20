#!/bin/python3

# need to convert this to a function so that it can loop throught all the files in the folder
# def printme( str ):
#   "This prints a passed string into this function"
#   print (str)
#   return


import hashlib

file = "/home/vfjr/Documents/Scripts/Python/IMG_3197.JPG" # Location of the file
BLOCK_SIZE = 65536 # The size of each read from the file

file_hash = hashlib.blake2b() # Create the hash object
with open(file, 'rb') as f: # Open the file to read it's bytes
    fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
    while len(fb) > 0: # While there is still data being read from the file
        file_hash.update(fb) # Update the hash
        fb = f.read(BLOCK_SIZE) # Read the next block from the file

print (file_hash.hexdigest()) # Get the hexadecimal digest of the hash
