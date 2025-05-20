import os
import shutil
from datetime import datetime

# Create a timestamp (e.g., "2025-04-30_143021")
timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')

def move_files_to_archive(source_dir, destination_dir):
    
    os.makedirs(destination_dir, exist_ok=True)
    destination_dir=destination_dir+"completed_"+timestamp
    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        # Determine the relative path from the source root
        rel_path = os.path.relpath(root, source_dir)
        dest_path = os.path.join(destination_dir, rel_path)

        # Create corresponding directories in destination
        os.makedirs(dest_path, exist_ok=True)

        # Move each file
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_path, file)
            shutil.move(src_file, dst_file)
            print(f"Moved file: {src_file} -> {dst_file}")

    print("All files and folders moved.")

