#convert a folder of jpg's to PDF's
#2017-07-15

#pre-reqs:
##Linux: sudo apt-get install libgraphicsmagick++1-dev libboost-python-dev
##MAC: 
## brew install graphicsmagick
## brew install boost-python
## sudo pip install pgmagick

import os
from os import listdir
from os.path import isfile, join 
from pgmagick import Image

mypath = "/Volumes/Storage/bookfiles" # path to your Image directory 

for each_file in listdir(mypath):
    if isfile(join(mypath,each_file)):
        image_path = os.path.join(mypath,each_file)
        pdf_path =  os.path.join(mypath,each_file.rsplit('.', 1)[0]+'.pdf')
        img = Image(image_path)
        img.write(pdf_path)
