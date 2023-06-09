"""
This script creates dummy files in the specified directory.
"""

import os


def create_dummy_files(directory, extensions, num_files_per_extension):
    """
    Creates dummy files in the specified directory.
    directory: string (path)
    extension: list of strings (extensions of the dummy files to create)
    num_files_per_extension: int (number of dummy files to create for each extension)
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the dummy files
    for extension in extensions:
        for i in range(num_files_per_extension):
            filename = "dummy_" + extension + "_" + str(i+1) + "." + extension
            filepath = os.path.join(directory, filename)
            with open(filepath, "w") as f:
                f.write(filepath)

if __name__ == "__main__":
    # Define the directory path where dummy files will be created
    directory = "./testdir"
    extensions = ["txt", "pdf", "png", "docx", "xlsx", "pptx", "zip", "exe"]
    num_files_per_extension = 25

    create_dummy_files(directory, extensions, num_files_per_extension)