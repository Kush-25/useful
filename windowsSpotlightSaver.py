# importing required packages
from pathlib import Path
import shutil
import os
import sys
 
# defining source and destination
# paths

src = (r"C:\Users\kushg\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")  

# Windows + R, then run %userprofile%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
# Copy and paste the location here for src as the source folder

trg = (r"C:\Users\kushg\Desktop\Here")
# Copy and paste the location here for src as the destination folder             
 
files=os.listdir(src)
 
# iterating over all the files in
# the source directory
for fname in files:
     
    # copying the files to the
    # destination directory
    shutil.copy2(os.path.join(src,fname), trg)       


def rename_files_to_jpg(folder_path):
    try:
        # Check if the folder path exists
        if not os.path.exists(folder_path):
            print("Folder not found.")
            return

        # Get a list of all files in the folder
        file_list = os.listdir(folder_path)

        # Iterate through each file and rename it to .jpg
        for filename in file_list:
            old_file_path = os.path.join(folder_path, filename)
            if os.path.isfile(old_file_path):
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_file_path = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")

        print("All files have been renamed to .jpg.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    folder_path = trg  # Replace this with the path to your folder
    rename_files_to_jpg(folder_path)       