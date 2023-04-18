"""
This script decrypts the files in the specified directory.
"""


import os
from Crypto.Cipher import AES
import pickle

def decrypt_files(directory, encryption_key):
    """
    Decrypts the files in the specified directory.
    directory: string (path)
    encryption_key: string (encryption key)
    """
    # Simulate the ransomware decryption
    for filename in os.listdir(directory):
        # Decrypt the file using AES encryption
        cipher = AES.new(encryption_key, AES.MODE_GCM)
        with open(os.path.join(directory, filename), "rb") as f:
            filedata = f.read()
            decrypted_data = cipher.decrypt(filedata)
            # Remove the padding from the decrypted data
            unpadded_data = decrypted_data.rstrip(b"\0")
        with open(os.path.join(directory, filename), "wb") as f:
            f.write(unpadded_data)


if __name__ == "__main__":
    # Define the directory path where the files to be decrypted are located
    directory = "./testdir"

    # Get the encryption key from the user converting it to bytes
    encryption_key = input("Enter the encryption key: ").encode()

    # Decrypt the files
    decrypt_files(directory, encryption_key)

    # get the original filenames from the pkl file
    with open("original_filenames.pkl", "rb") as f:
        original_filenames = pickle.load(f)
     
    # Rename the files to their original names
    for filename in os.listdir(directory):
        os.rename(os.path.join(directory, filename), os.path.join(directory, original_filenames[filename]))



    print("Files decrypted successfully.")