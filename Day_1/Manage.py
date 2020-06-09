import os

this_file_path = os.path.abspath(__file__)
base_dir_path = os.path.dirname(this_file_path)
folder_name = os.path.join(base_dir_path, "py_template")

if os.path.exists(folder_name):
    file_name = os.path.join(folder_name, "UniqueText.txt")
    with open(file_name, 'w') as file_object:
        file_object.write("Hey you just create new file")

else:
    os.makedirs(folder_name)
    file_name = os.path.join(folder_name, "UniqueText.txt")
    with open(file_name, 'w') as file_object:
        file_object.write("Hey you just create directory and also create file inside the directory")


