import os
import re

def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\herrm\Desktop\dev\rename_files\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)
    os.chdir(r"C:\Users\herrm\Desktop\dev\rename_files\prank")
    # for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+re.sub("[0-9]", "", file_name))
        os.rename(file_name, re.sub("[0-9]", "", file_name))
    os.chdir(saved_path)

rename_files()
