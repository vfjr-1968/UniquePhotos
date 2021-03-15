
import time 
import os 
  
  
# Getting the path of the file 
f_path = "//home/vfjr/Pictures/1761.JPG"
  
# Obtaining the creation time (in seconds) 
# of the file/folder (datatype=int) 
t = os.path.getctime(f_path) 
  
# Converting the time to an epoch string 
# (the output timestamp string would 
# be recognizable by strptime() without 
# format quantifers) 
t_str = time.ctime(t) 
  
# Converting the string to a time object 
t_obj = time.strptime(t_str) 

print(t_obj)  
# Transforming the time object to a timestamp 
# of ISO 8601 format 
form_t = time.strftime("%Y-%m-%d %H:%M:%S", t_obj) 
  
# Since colon is an invalid character for a 
# Windows file name Replacing colon with a 
# similar looking symbol found in unicode 
# Modified Letter Colon " " (U+A789) 
form_t = form_t.replace(":", "꞉") 
message = 'form_t = ' + form_t
print(message)  
# Renaming the filename to its timestamp 
#os.rename( 
#    f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1]) 
