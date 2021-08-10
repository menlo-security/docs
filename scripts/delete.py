import os, glob


try:
    os.rmdir('./7255-Documentation_Hub-html5/out')
    os.rmdir('./7255-Documentation_Hub-html5')
    os.remove('./7255-Documentation_Hub-html5_-Upload_to_GitHub.zip')
    print('Deleted unneeded sub-directories...')
    
except:
   print('[ERROR!] Unable to delete files.')

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.