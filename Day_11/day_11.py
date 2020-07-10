import os
import shutil
from zipfile import ZipFile

dir_list = os.listdir(os.path.dirname(__file__))
dir_name = os.path.dirname(__file__)

for item in dir_list:
    shutil.make_archive(item, 'zip', dir_name)
