import os
import shutil

current_dir = os.getcwd()

for file in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(file)

    try:
        if file_ext in '':
            pass
        elif file_ext in ('.docx' or '.txt'):
            print(os.path.join(filename, file_ext))

    except FileNotFoundError:
        pass
