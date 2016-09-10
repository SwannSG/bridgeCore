# *.pbn


import fnmatch
import os
 
rootPath = '/home/swannsg/Downloads'
pattern = '*.pbn'
 
for root, dirs, files in os.walk(rootPath):
        for filename in files:
            if filename.endswith(('.pbn', '.PBN')):
                print( os.path.join(root, filename))



#   for filename in fnmatch.filter(files, pattern):
