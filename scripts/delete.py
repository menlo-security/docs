import os, glob


try:
    os.rmdir('./41857-Menlo_Security_Documentation_v0-html5_1642543602.4066/out')
    os.rmdir('./41857-Menlo_Security_Documentation_v0-html5_1642543602.4066')
    os.remove('./41857-Menlo_Security_Documentation_v0-html5_1642543602.4066.zip')
    print('Deleted unneeded sub-directories...')
    
except:
   print('[ERROR!] Unable to delete files.')

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.
