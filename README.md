<h1>Stress-test</h1>
<p>This tool suite aims at emulating ransomware behaviour in order to evaluate EDR/EPP performance and detection capabilities. This tool should not present any danger : its behaviour is known because we coded it from scratch, publish the source code, and also proceed to security code review.  

You can download the binaries : <a href="https://github.com/BlueTrusty/stress-test/releases"> here</a>.

Once  downloaded, extract the "stresstest-windows-executable.zip" archive in a directory of your choice, then run the executables. The binaries are standalone, you do not need to install anything else.

After you have run the test, you can simply delete the "testdir" directory that was created as well as the binaries themselves.
</p>
<h2>The tool is composed of 3 binaries:</h2>
<ul>
    <li>
        <h3>Step 1:</h3>
        <code>step_1_create_dummy_files.exe</code>
        <p>The binary generates dummy files with various extensions (txt, pdf, png, xlsx...), they contain their own path and filename. The dummy files can be found in the "testdir" directory that is created where you run the binary.</p>
    </li>
    <li>
        <h3>Step 2:</h3>
        <code>step_2_encrypt_files.exe</code>
        <p>This binary encrypts the content with a randomly generated 16 bytes key. It changes the name of the files and modifies the extensions as well. All of the new extensions are known ransomware extensions. In order for the files to be decrypted (optional), the key is stored in a file named "encryption_key.txt" in the same directory as testdir. The original filenames are stored in a pkl file named "original_filenames.pkl" in order to be restored.
        <strong>This step should trigger your EPP/EDR.</strong>
        </p>
    </li>
    <li>
        <h3>Step 3 (optional):</h3>
        <code>step_3_decrypt_files.exe</code>
        <p>This binary decrypts the files and restores their original name and extension.</p>
    </li>
</ul>
<p> FYI:  This test is included in our "ransomware stress-test" service ; you can learn more about it here: <a href="https://stresstest.bluetrusty.com/">https://stresstest.bluetrusty.com/</a>.</p>
