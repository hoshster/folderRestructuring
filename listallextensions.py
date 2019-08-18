import os
import shutil
import time

movietypes = ('.3gp', '.wmv', '.asf', '.avi', '.flv', '.mov', '.mp4', '.ogm', '.mkv',
'. mpg', '.mpg', '.nsc', '.nsv', '.nut', '.a52', '.tta', '.wav', '.ram', '.asf',
'.wmv', '. ogg', '.mka', '.vid', '.lac', '.aac', '.dts', '.tac',
'.dts', '.mbv')

filewrite = open('H:\\Movies from download folder\\Logs\\logstest.txt', 'w')
dir_src = "C:\\Users\\Jeremy\\Downloads\\"
dir_dst = "H:\\Movies from download folder\\"

for root, dirs, files in os.walk(dir_src):
    for file in files:
        if file.endswith(movietypes) == True:
           filestr = str(file)
           locationoffoundfile = os.path.realpath(os.path.join(root,filestr))
           folderitwasin = locationoffoundfile.replace(dir_src,'')
           folderitwasin = folderitwasin.replace(filestr,'')
           pathofdir = os.path.realpath(root) + "\\"
           if pathofdir != dir_src:
                src_file = locationoffoundfile
                dst_file = dir_dst + folderitwasin + filestr
                os.rename(src_file, dst_file) #****This line is the line im having issues with***
                print src_file
                print dst_file
                filewrite.write(file + " " + "needs to have dir and file moved Moved!" + '\n')
           else:
                src_file = os.path.join(dir_src, file)
                dst_file = os.path.join(dir_dst, file)
                print src_file
                print dst_file
                shutil.move(src_file, dst_file)
                filewrite.write(os.path.dirname(file) + '\n')
                filewrite.write(file + " " + "needs to have file moved Moved!" + '\n')
filewrite.close()