# diarycrypto

Creates and encrypts a diary for you, which can be re-opened and edited more if you know the password! This works if you are using Windows and notepad.exe is your default program for opening .txt files. To create/edit/view the diary, use command prompt in the appropriate directory and do:

py diarycrypto.py [password]

The encryption is not very strong at all. It's just a repeating XOR cipher, which should still be enough to protect your diary from people lacking computer savvy. 
