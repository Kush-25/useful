import os

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
    folder_path = (r"C:\Users\kushg\Desktop\Here")  # Replace this with the path to your folder
    rename_files_to_jpg(folder_path)