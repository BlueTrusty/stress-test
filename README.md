# stress-test

A tool suite aimed at emulating ransomware behaviour in order to evaluate EDR/EPP performance and detection capabilities.

The tool is delivered with 3 binaries :

- ## step #1 : 
    ### step_1_create_dummy_files.exe
    
    The binary generates dummy files with various extensions (txt , pdf , png), they contain their own path and filename.

    The dummy files can be found in the "testdir" directory that is created where you run the binary.

- ## step #2 :
    ### step_2_encrypt_files.exe

    This binary encrypts the content with a randomly generated 16 bytes key.

    It changes the name of the files and modifies the extensions as well.

    All of the new extensions are known ransomware extensions.

    In order for the files to be decrypted (optionnal), the key is stored in a file named "encryption_key.txt" in the same directory as testdir. The original filenames are stored in a pkl file named "original_filenames.pkl" in order to be restored.

- ## step #3 (optionnal) :

    ### step_3_decrypt_files.exe

    This binary decrypts the files and restores their original name and extension.

    Will likely triger your EPP/EDR ! 

** STILL IN EARLY BETA **
