# Import libraries

import os  # Interact with the operating system for file & folder operations

# Define function
def rename_images(folder_path, prefix="image"):
    
    # Check file
    if not os.path.exists(folder_path):
        print("Invalid folder path")
        return

    # List all files & folders in the specified directory
    all_files = os.listdir(folder_path)

    # Filter only images
    image_extensions = (".jpg", ".png")  # Common image extensions
    image_files = [f for f in all_files if f.lower().endswith(image_extensions)]  # Filter images

    # Check images
    if not image_files:
        print("No images found")
        return

    # Sort images
    image_files.sort()

    # Start numbering from 1
    count = 1

    # Loop through each image and rename
    for image in image_files:
        extension = os.path.splitext(image)[1]  # Get file extension
        new_name = f"{prefix}{count}{extension}"  # Create new name: image1.jpg
        old_path = os.path.join(folder_path, image)  # Old file path
        new_path = os.path.join(folder_path, new_name)  # New file path

        # Check new file
        if os.path.exists(new_path):
            print(f"'{image}', '{new_name}' new file exists")
        else:
            os.rename(old_path, new_path)  # Rename file
            print(f"Renamed '{image}' to '{new_name}'")  # Review image file name changes
            count += 1 

    print("Images renamed")

# User input and run function
folder = input("Images folder: ")  # Folder path input
prefix = input("Prefix: ")
rename_images(folder, prefix)  # Call function
