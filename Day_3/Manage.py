import os
import shutil

"documents" = [".docx", ".txt"]
current_dir = os.getcwd()

for file in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(file)

    try:
        if file_ext in '':
            pass
        elif any(file_ext for x in docs):
            print(os.path.join(filename, file_ext))

    except FileNotFoundError:
        pass
