import os, shutil, glob

_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'AUD Study Guide', 'CPA AUD 2020-v0.4.91327')
_np = os.path.join(os.path.expanduser('~'), 'Desktop', 'AUD Study Guide', 'sortedFolders')
_fdn = ['intro.pref', 'mem.pub.prac', 'memb.bus', 'oth.memb']

os.chdir(_path)

# Move file with the specific names
for item in _fdn:
   for dirpath, dirnames, filenames in os.walk(_path):
       for filename in dirnames:
           if item == filename:
               _foundFolder = os.path.join(dirpath, filename)
               shutil.move(_foundFolder, _np)

# Rename the folder name based on the provied list.
os.chdir(_np)
os.getcwd()
for index, item in enumerate(_fdn):
    for dirpath, dirnames, filenames in os.walk(_np):
        for filename in dirnames:
            if item == filename:
                    _dst = str(index+1) + '_' + item
                    _nn = os.rename(filename, _dst)
                    # print(filename)



# Delete Empty folders from a defined path
for root, dirs, files in os.walk(_np, topdown=False):
       for name in dirs:
           try:
               if len(os.listdir( os.path.join(root, name) )) == 0: #check whether the directory is empty
                   print( "Deleting", os.path.join(root, name) )
                   try:
                       os.rmdir( os.path.join(root, name) )
                   except:
                       print( "FAILED :", os.path.join(root, name) )
                       pass
           except:
               pass