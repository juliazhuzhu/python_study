#!/usr/bin/python
import os,sys

#if we run this script from other places, the CWD moves with us (it’s the directory
#where we type commands), and Python adds a directory to the front of the module
#search path that allows the script to still see files in its own home directory. For instance,
#when running from one level up ( .. ), the System name added to the front of sys.path
#will be the first directory that Python searches for imports within whereami.py; it points
#imports back to the directory containing the script that was run. Filenames without
#Comcomplete paths, though, will be mapped to the CWD the System subdirectory nested there


print('my os.getcwd =>', os.getcwd())
print('my sys.path =>', sys.path[:3])
input()
