import os


print(os.name)
#print(os.machine())

#print(os.cpu_count())
cpu_count = os.cpu_count()
print (cpu_count)
print(os.getcwd())
print(os.listdir('/home'))
print(os.getuid())
print(os.uname())