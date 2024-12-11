#Task 1 Directory Inspector
"""Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents."""


import os

def list_directory_contents(path):
    subfolders = [] # Empty list to add contents
    for entry in os.scandir(path):
        if entry.is_dir():  # Check if it's a directory
            subfolders.append(entry.path)  # Add the directory path
            subfolders.extend(list_directory_contents(entry.path))  # Recursively get subdirectories
    return subfolders
