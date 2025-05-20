import os

def remove_empty_folders(root_dir):
    # Walk from bottom up to avoid errors when deleting parent before children
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)
            print(f"Removed empty folder: {dirpath}")


