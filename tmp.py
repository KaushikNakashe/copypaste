import os

def print_directory_structure(root_dir, indent=0):
    """Recursively prints the directory structure."""
    try:
        # Print the current directory
        print(' ' * indent + os.path.basename(root_dir) + '/')
        indent += 4  # Increase indentation for child directories

        # List all files and directories in the current directory
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                # Recursively print directory structure
                print_directory_structure(item_path, indent)
            else:
                # Print file names
                print(' ' * indent + item)
    except PermissionError as e:
        print(' ' * indent + "[Permission Denied]")

# Example usage
root_directory = 'D:\\Gryphos_portal_ocr_V0.5'
print_directory_structure(root_directory)
