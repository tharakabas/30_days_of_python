import os
import shutil
from zipfile import ZipFile

dir_list = os.listdir(os.path.dirname(__file__))
dir_name = os.path.dirname(__file__)

for item in dir_list:
    filename = item + '.zip'
    with ZipFile(filename,'w') as zip:
        zip.write(item)
