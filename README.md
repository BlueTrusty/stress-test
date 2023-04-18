# stress-test

A tool suite aimed to emulate ranswomare behaviour in order to evaluate EDR/EPP performance and detection capabilities.

The tool is delivered with 3 binaries :
- step #1 : create 9 dummy files (txt , pdf , png )
- step #2 : encrypt the content with randomly generated key ; change the extension of these 9 files to 9 ; create a pkl file containing the mapping old<>new file
- step #3 (optionnal) : decrypt and reverse the 9 file to their original content and filename 
