import os, shutil, glob

_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'sourceDir')
_np = os.path.join(os.path.expanduser('~'), 'Desktop', 'sourceDir', 'sortedFolders')
_fdn = ["equity.recogn.25", "equity.recogn.30"]

os.chdir(_path)
# Move file with the specific names
for dirpath, dirnames, filenames in os.walk(_path):
    for filename in dirnames:
        if filename == _fdn:
            filename = os.path.join(dirpath, filename)
            shutil.move(filename, _np)
            for filename in _fdn:
                f = os.path.join(dirpath, filename)
                shutil.move(f, _np)    

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