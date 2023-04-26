<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Stress-test</title>
	<style>
		body {
			font-family: Arial, Helvetica, sans-serif;
			font-size: 16px;
			line-height: 1.5;
			margin: 0;
			padding: 0;
		}
		h1 {
			font-size: 32px;
			margin-top: 40px;
			margin-bottom: 20px;
			/* text-align: center; */
			letter-spacing: 1px;
		}
		h2 {
			font-size: 24px;
			margin-top: 30px;
			margin-bottom: 15px;
			letter-spacing: 1px;
		}
		h3 {
			font-size: 20px;
			margin-top: 25px;
			margin-bottom: 10px;
			letter-spacing: 1px;
		}
		ul {
			list-style: none;
			margin: 0;
			padding: 0;
		}
		li {
			margin-bottom: 10px;
		}
		code {
			border: 1px solid #ccc;
			border-radius: 3px;
			padding: 2px 5px;
			font-family: Consolas, Monaco, monospace;
			font-size: 14px;
		}
	</style>
</head>
<body>
	<h1>Stress-test</h1>
	<p>A tool suite aimed at emulating ransomware behaviour in order to evaluate EDR/EPP performance and detection capabilities.</p>
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
			<p>This binary encrypts the content with a randomly generated 16 bytes key. It changes the name of the files and modifies the extensions as well. All of the new extensions are known ransomware extensions. In order for the files to be decrypted (optional), the key is stored in a file named "encryption_key.txt" in the same directory as testdir. The original filenames are stored in a pkl file named "original_filenames.pkl" in order to be restored.</p>
		</li>
		<li>
			<h3>Step 3 (optional):</h3>
			<code>step_3_decrypt_files.exe</code>
			<p>This binary decrypts the files and restores their original name and extension. Will likely triger your EPP/EDR!</p>
		</li>
	</ul>
	<p><strong>STILL IN EARLY BETA</strong></p>
</body>
</html>
