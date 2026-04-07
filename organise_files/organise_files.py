# Import libraries
import os
import shutil

# Find Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Map file extensions to folders
extensions = {
    ".png": "Images",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
}

# Loop through all items on Desktop
for filename in os.listdir(desktop_path): # List files and folders on Desktop
    file_path = os.path.join(desktop_path, filename) # Check full path

    # Check if this path is a file
    if os.path.isfile(file_path) and not filename.startswith("."):
        extension = os.path.splitext(filename)[1].lower() # Split filename into name and extension and get only extension
        if extension in extensions: # Check file type
            folder_name = extensions[extension] # Find folder name from the dictionary
            folder_path = os.path.join(desktop_path, folder_name) # Create full 

            # Check if folder exists
            if not os.path.exists(folder_path):
                os.mkdir(folder_path) # Create folder if not found

            # Move file into the correct folder
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)
            print(f"Moved {filename} → {folder_name}")
        else:
            print(f"Skipped {filename}:") # Unknown file type
    else:
        print(f"Skipped {filename}") # Hidden file and folder
        
print("\nFiles are organised into folders.")