import os
import shutil

# get current working directory path
dir_name = os.path.dirname(__file__)

# Map file extensions
ext_dict = {
    "Document": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                 ".pub", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                 ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx", ".txt"],

    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv",
              "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],

    "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt",
              ".mpg", ".mpeg", ".3gp", ".mkv"],

    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif",
               ".psd"]
}

"""
Using this method first list all directories in current working directory and go 
each by each check whether are they file or folder if file that file match with extension
dictionary and move them to matched folder.when move files into folders first check destination
file exist if not first create destination folder and move if destination folder exist 
check current file is in the folder if it is in the folder simply pass that step and go
forward if not exist move file to the folder  
"""


def organizer(file_type, dest_folder):
    for names in os.listdir(dir_name):
        file_names, extensions = os.path.splitext(names)
        if extensions in ext_dict[file_type]:
            if os.path.exists(os.path.join(dir_name, dest_folder)):
                if os.path.exists(os.path.join(dir_name, dest_folder, names)):
                    pass
                else:
                    shutil.move(os.path.join(dir_name, names), os.path.join(dir_name, dest_folder))
            else:
                os.makedirs(os.path.join(dir_name, dest_folder))
                if os.path.exists(os.path.join(dir_name, dest_folder, names)):
                    pass
                else:
                    shutil.move(os.path.join(dir_name, names), os.path.join(dir_name, dest_folder))


organizer('Document', 'Documents')
organizer('Audio', 'Audios')
organizer('Video', 'Videos')
organizer('Images', 'Images')
