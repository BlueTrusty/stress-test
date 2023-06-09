"""
This script decrypts the files in the specified directory.
"""

import os
from Crypto.Cipher import AES
import pickle
from Crypto.Util.Padding import unpad

def decrypt_file(filename, encryption_key):
    """
    Decrypts a file.
    filename: string
    encryption_key: string
    """
    # Decrypt the file using AES encryption
    with open(filename, "rb") as f:
        nonce = f.read(16)
        filedata = f.read()
        cipher = AES.new(encryption_key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = cipher.decrypt(filedata)
        # Remove the padding from the decrypted data
        unpadded_data = unpad(decrypted_data, AES.block_size)
    with open(filename, "wb") as f:
        f.write(unpadded_data)

def decrypt_files(directory, encryption_key):
    """
    Decrypts the files in the specified directory.
    directory: string (path)
    encryption_key: string
    """
    # get the original filenames from the pkl file
    with open("original_filenames.pkl", "rb") as f:
        original_filenames = pickle.load(f)
     
    # Decrypt the files
    for filename in os.listdir(directory):
        decrypt_file(os.path.join(directory, filename), encryption_key)
        # Rename the files to their original names
        os.rename(os.path.join(directory, filename), os.path.join(directory, original_filenames[filename])) 

    


if __name__ == "__main__":
    # Define the directory path where the files to be decrypted are located
    directory = "./testdir"

    # Get the encryption key from the user converting it to bytes
    encryption_key_int = int(input("Enter the encryption key: "))
    encryption_key = encryption_key_int.to_bytes(16, "big")
    
    # Decrypt the files
    decrypt_files(directory, encryption_key)

    print("Files decrypted successfully.")