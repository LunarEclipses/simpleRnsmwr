import os
#un-comment line 3 if you want this to run
#from cyptography.fernet import Fernet

#find files


files = []

for file in os.listdir():
    if file == "bigballs.py" or file=="thekey.key" or file=="smallballs.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key:
    secretkey=key.read()
    
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
