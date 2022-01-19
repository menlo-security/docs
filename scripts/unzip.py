from zipfile import ZipFile
import fnmatch
import re, os
import glob

def main():
    
    print('Unzipped files...')
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile('41857-Menlo_Security_Documentation_v0-html5_1642543602.4066.zip', 'r') as zipObj:
       # Extract all the contents of zip file in current directory
       zipObj.extractall()


if __name__ == '__main__':
   main()

else:
    print('[ERROR!] Unable to unzip files.')


# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.
