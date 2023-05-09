<h1>Stress-test</h1>
<p>This tool suite aims at emulating ransomware behaviour in order to evaluate EDR/EPP performance and detection capabilities. This tool will not endanger or even access any of your personal files, its behaviour is known and trusted. 

You can download the binaries here: <a href="https://github.com/BlueTrusty/stress-test/releases"> Releases</a>.

You need to download and then extract the "stresstest-windows-executable.zip" archive in order to run the executables.

You can simply run the binaries in a directory of your choice.

After you have run the test, you can simply delete the "testdir" directory that is created where you run the binaries as well as the binaries themselves.
</p>
<h2>The tool is delivered with 3 binaries:</h2>
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
        This step should trigger your EPP/EDR.
        </p>
    </li>
    <li>
        <h3>Step 3 (optional):</h3>
        <code>step_3_decrypt_files.exe</code>
        <p>This binary decrypts the files and restores their original name and extension.</p>
    </li>
</ul>
<p> FYI:  This test is included in our stress-test that you can learn more about here: <a href="https://stresstest.bluetrusty.com/">https://stresstest.bluetrusty.com/</a>.</p>
