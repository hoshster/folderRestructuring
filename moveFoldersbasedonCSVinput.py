#!/usr/bin/python
# Version 1
## Show menu ##

import os, shutil, glob, re, time
from os import listdir
from os.path import isfile, join
from datetime import datetime
from fnmatch import fnmatch
import tkinter as tk
import csv

start = time.time()

### Messages
message_1 = "Select a Source Directory to Continue: "
message_2 = "Select a Destination Directory to Continue: "
message_3 = "Select CSV File to Continue: "


### Create default OUT folder in Desktop
print(os.getcwd())
os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))

if not os.path.exists('outFolder'):
    os.mkdir('outFolder')
else:
    pass

# _path = os.path.join(os.path.expanduser('~'), 'Desktop', 'FAR', 'CPA FAR 2020.json', 'CPA FAR 2020')
_path = input(message_1)

_np = os.path.join(os.path.expanduser('~'), 'Desktop', 'outFolder')

# _csvin = '/Users/hoshiyar/Desktop/FAR.csv'
_csvin = input(message_3)

with open(_csvin, 'r') as f:
    cr = csv.reader(f)
    list1 = list(cr)
    _ftbc = []
    for sublist in list1:
        for val in sublist:
            _ftbc.append(val)
# print(_ftbc)

################ Do not make any changes to the below code ################

#Change Directory path...

os.chdir(_path)

# Strip/Cleanup spaces from folder names
_stsps = []
for i in _ftbc:
    str(i).replace(' ','')
    _stsps.append(i)
# print(_stsps)

# Find and Replace ".json" keyword from filesnames
_fdn = [sub.replace('.json', '') for sub in _stsps]
# print(_fdn)

r = len(_fdn)
print(f'{r} Directories need to be processed ...')
# for index, item in enumerate(_fdn):
#     print(index+1, item)

################ Remove Empty Directories ################
os.chdir(_path)

while True:
    to_delete = []
    for root, dirs, _ in os.walk('.'):
        for d in dirs:
            full_path = os.path.join(root, d)
            if all(s.startswith('.') for s in os.listdir(full_path)):
                to_delete.append(full_path)

    if to_delete:
        for p in to_delete:
            shutil.rmtree(p)
    else:
        break

################ Main Code ################

os.chdir(_path)

_fdn.reverse()
_rfdn = _fdn

# Move file with the specific names
for item in _rfdn:
   for dirpath, dirnames, filenames in os.walk(_path):
       for filename in dirnames:
           if item == filename:
               _foundFolder = os.path.join(dirpath, filename)
               shutil.move(_foundFolder, _np)


#Rename Folders based on the list index values

_fdn.reverse()
_nfdn = _fdn
os.chdir(_np)
os.getcwd()
for index, item in enumerate(_nfdn):
    for dirpath, dirnames, filenames in os.walk(_np):
        for filename in dirnames:
            if item == filename:
                    i = str(index+1)
                    _dst = i.zfill(3) + '_' + item
                    _nn = os.rename(item, _dst)
                    # print(filename)



################  Writing log to a text file for the moved files: ################


dirName = _np
filename = dirName.split('\\')[-1]


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)

    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in dirnames]

    start = time.time()
    now = datetime.now()
    d3 = now.strftime("%m/%d/%Y %H:%M:%S")

    # Print the files    
    with open(dirName + '_Report.txt', 'w') as f:
        # Write-Overwrites
        print('Conversion Detailed Report\n', file=f)
        print('***********************************************************************', file=f)
        print('Original Directory Path   : ',dirName , file=f)
        print('Time Stamp                : ', d3, file=f)
        print('Total Files in Directory  : ', len(listOfFiles), ' Files', file=f)
        print("Tool Run Time             :  %.2fms"%(time.time()-start), file=f)
        print("EXE Created By            :  Python v3", file=f)
        print('Version                   : ' , 'v1', file=f)
        print('***********************************************************************', file=f)
        print('Detailed Files Summary from "'+ filename + '" : \n', file=f)

        for index, curelem in enumerate(listOfFiles):
                print(str(index+1) + ") ", curelem, file=f)

print("Process Completed by the Script... \n Total Time Taken :  %.2fms"%(time.time()-start))

