import os
import shutil
from datetime import datetime

def organize_paths(paths):
    for path in paths:
        if not os.path.exists(path):
            print(f"Path does not exist: {path}")
            continue
        
        # Process files and directories in the current path (non-recursive)
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            
            if os.path.isdir(item_path):
                handle_directory(item_path, path)
            elif os.path.isfile(item_path):
                handle_file(item_path, path)

def handle_directory(dir_path, parent_path):
    # Get modification month for the directory
    mod_time = os.path.getmtime(dir_path)
    month_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")
    
    # Create the 'directories' subfolder under the month folder
    month_dir_path = os.path.join(parent_path, month_folder, "directories")
    os.makedirs(month_dir_path, exist_ok=True)
    
    # Move the directory
    shutil.move(dir_path, os.path.join(month_dir_path, os.path.basename(dir_path)))

def handle_file(file_path, parent_path):
    # Get modification month for the file
    mod_time = os.path.getmtime(file_path)
    month_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")
    
    # Determine file extension (or 'unknown' if no extension)
    file_extension = os.path.splitext(file_path)[1][1:].lower() or "unknown"
    
    # Create the subfolder for the file extension under the month folder
    extension_dir_path = os.path.join(parent_path, month_folder, file_extension)
    os.makedirs(extension_dir_path, exist_ok=True)
    
    # Move the file
    shutil.move(file_path, os.path.join(extension_dir_path, os.path.basename(file_path)))

# Example usage
paths_to_organize = [
    "/home/p3jman/Downloads",
]

organize_paths(paths_to_organize)
