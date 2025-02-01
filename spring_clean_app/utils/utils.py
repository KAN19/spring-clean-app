import os


def create_file(file_path, content):
    """Create a file with the specified content."""
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Created file: {file_path}")


def create_folder(folder, exist_ok):
    os.makedirs(folder, exist_ok=exist_ok)
    print(f"Created folder: {folder}")


def create_folder(base_path, folder, exist_ok=True):
    # Create the full path
    full_path = os.path.join(base_path, folder)
    # Use os.makedirs to create the nested folder structure
    os.makedirs(full_path, exist_ok=exist_ok)
    print(f"Created: {full_path}")


def create_folders(base_path, folder_structure, exist_ok=True):
    for val in folder_structure.values():
        create_folder(base_path, val)
