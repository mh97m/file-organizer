import os
import shutil
from datetime import datetime
import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def organize_paths(paths):
    print(Fore.BLUE + "Starting organization of paths...\n")
    for path in paths:
        if not os.path.exists(path):
            print(Fore.RED + f"Path does not exist: {path}")
            continue

        print(Fore.YELLOW + f"Processing path: {path}\n")

        # Process files and directories in the current path (non-recursive)
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            
            # Ignore folders with names matching the YYYY-MM pattern
            if os.path.isdir(item_path) and re.match(r"^\d{4}-\d{2}$", item):
                print(Fore.CYAN + f"Skipping folder (already organized): {item}")
                continue

            if os.path.isdir(item_path):
                handle_directory(item_path, path)
            elif os.path.isfile(item_path):
                handle_file(item_path, path)

    print(Fore.GREEN + "\nOrganization complete!")

def handle_directory(dir_path, parent_path):
    mod_time = os.path.getmtime(dir_path)
    month_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")

    month_dir_path = os.path.join(parent_path, month_folder, "directories")
    os.makedirs(month_dir_path, exist_ok=True)

    target_path = os.path.join(month_dir_path, os.path.basename(dir_path))
    shutil.move(dir_path, target_path)

    print(Fore.MAGENTA + f"Moved directory: {os.path.basename(dir_path)}")
    print(Fore.WHITE + f"  From: {dir_path}")
    print(Fore.WHITE + f"  To:   {target_path}\n")

def handle_file(file_path, parent_path):
    mod_time = os.path.getmtime(file_path)
    month_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m")

    file_extension = os.path.splitext(file_path)[1][1:].lower() or "unknown"
    extension_dir_path = os.path.join(parent_path, month_folder, file_extension)
    os.makedirs(extension_dir_path, exist_ok=True)

    target_path = os.path.join(extension_dir_path, os.path.basename(file_path))
    shutil.move(file_path, target_path)

    print(Fore.GREEN + f"Moved file: {os.path.basename(file_path)}")
    print(Fore.WHITE + f"  From: {file_path}")
    print(Fore.WHITE + f"  To:   {target_path}\n")

# Example usage
paths_to_organize = [
    "/home/p3jman/Downloads",
]

organize_paths(paths_to_organize)
