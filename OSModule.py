# OS MODULE:---------------------------------------------


import os
print(dir(os))
print(os.getcwd())
os.chdir("C://")
print(os.getcwd())
f = open("harry.txt")
print(os.listdir("C://"))
os.makedirs("This/that")
os.rename("HRX.txt","anshdhairya.txt")

print(os.environ.get('path'))

print(os.path.join("C://","harry.txt"))
print(os.path.exists("C://"))