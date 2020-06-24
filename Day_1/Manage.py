import os

base_dir_path = os.path.dirname(__file__)  # get current working directory
folder_name = os.path.join(base_dir_path, "py_template")

# Checking to folder existing
if os.path.exists(folder_name):
    file_name = os.path.join(folder_name, "UniqueText.txt")
    with open(file_name, 'w') as file_object:
        file_object.write("Hey you just create new file")

else:
    os.makedirs(folder_name)
    file_name = os.path.join(folder_name, "UniqueText.txt")
    with open(file_name, 'w') as file_object:
        file_object.write("Hey you just create directory and also create file inside the directory")
