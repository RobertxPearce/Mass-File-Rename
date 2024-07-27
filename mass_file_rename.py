import os

def rename_files_in_folder(folder_path):
    # List all files in the folder.
    files = os.listdir(folder_path)
    
    # Initialize a counter.
    counter = 1
    
    # Loop to iterate through file.
    for file_name in files:
        # Create new file name with counter.
        new_file_name = f"Covers_{counter:03d}{os.path.splitext(file_name)[1]}"
        
        # Create the full file paths.
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename the file.
        os.rename(old_file_path, new_file_path)
        
        # Increment the counter.
        counter += 1
    # Print completion message.
    print("Files have been renamed successfully!")

# Variable for folder path. ***UPDATE WITH FOLDER PATH***
folder_path = r'C:\'

# Call function to rename files.
rename_files_in_folder(folder_path)
