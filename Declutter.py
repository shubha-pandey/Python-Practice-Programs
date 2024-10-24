'''
Write a program to clear the clutter inside a folder on the computer.
Use OS module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder.
Do the same for other file formats.
'''


import os

files = os.listdir("OSFiles")                                                # folder name
i=1
for file in files :
    if file.endswith(".png") :                                               # file type
        os.rename(f"OSFiles/{file}",f"OSFiles/{i}.png")                      # original name, new name
        i = i + 1