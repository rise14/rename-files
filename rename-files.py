import os
import shutil

base_dir = 'downloads'       # Where your folders are
collected_dir = 'collected'  # Where renamed files will go

# Make sure the destination folder exists
os.makedirs(collected_dir, exist_ok=True)

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)

    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)

        if not files:
            continue

        # Take the first file only
        old_file_path = os.path.join(folder_path, files[0])
        _, ext = os.path.splitext(old_file_path)

        # Clean up extension and folder name
        new_file_name = folder.strip() + ext
        new_file_path = os.path.join(folder_path, new_file_name)
        final_destination = os.path.join(collected_dir, new_file_name)

        try:
            # Rename file to match folder name
            os.rename(old_file_path, new_file_path)

            # Move the renamed file to the collected folder
            shutil.move(new_file_path, final_destination)

            # Delete the original folder
            os.rmdir(folder_path)

            print(f"Moved and deleted folder: {folder}")
        except Exception as e:
            print(f"Error in '{folder}': {e}")