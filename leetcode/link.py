#!/usr/bin/python
"""
A script to create a soft link pointing to the most recent problem.
Will glob all directories and find the most recent created one.
"""
from __future__ import print_function #in case of using python 2.x print
import glob #glob all dir/files
import os #for getting timestamp

if os.path.islink("latest"): #if existing latest softlink, remove it
    print("Existed latest symlink.")
    os.unlink("./latest")
files = glob.glob("*")#glob all files


dirs = list(filter(lambda x:os.path.isdir(x),files)) #filter all dir
print("found dirs:")
print (list(dirs))
dirs.sort(key=lambda x: os.path.getmtime(x)) #sort all dir name based on its edit time
print("sorted dir:")
print(dirs)
src = "./"+dirs[-1] #get the most recent one

print("New pointer to "+src)
os.symlink(src,"./latest") #create symlink
