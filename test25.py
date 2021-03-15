
# import OS module 
import os, tkinter
from tkinter import messagebox

print (tkinter.Tcl().eval('info patchlevel'))
messagebox.showinfo("Title", "a Tk MessageBox")

# Get the list of all files and directories 
path = "/home/vfjr/Documents/Scripts/Python/"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :") 
  
# prints all files 
print(dir_list) 

