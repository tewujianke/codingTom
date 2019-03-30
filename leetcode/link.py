#!/usr/bin/python
"""
A script to create a soft link pointing to the most recent problem.
Will glob all directories and find the most recent created one.
"""
from __future__ import print_function
import glob
import os

if os.path.islink("latest"):
    print("Existed latest symlink.")
    os.unlink("./latest")
files = glob.glob("*")


dirs = list(filter(lambda x:os.path.isdir(x),files))
print("found dirs:")
print (list(dirs))
dirs.sort(key=lambda x: os.path.getmtime(x))
print("sorted dir:")
print(dirs)
src = "./"+dirs[-1]

print("New pointer to "+src)
os.symlink(src,"./latest")
