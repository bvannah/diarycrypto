import os
import sys
import psutil
import time

def decrypt(ciphertext, key):
	plaintext = ""
	i=0
	for ch in ciphertext:
		plaintext += chr(ord(ch) ^ ord(key[i]))
		i+=1
		i=i%len(key)
	return plaintext

def edit(file):
	os.startfile(file)
	i=False
	while(i!=True):
		i=True
		for p in psutil.process_iter():
			if(p.name() == "notepad.exe"):
				i=False
				break
		time.sleep(1)
	return




if __name__ == '__main__':
	key=sys.argv[1]
	filename="diary.txt"
	if(os.path.isfile(filename) != True):
		f=open(filename, 'w')#just to make the file
		f.close()
	f=open(filename, 'r')
	ciphertext = f.read()
	plaintext=decrypt(ciphertext, key)
	edits=open("edits.txt", "w")
	edits.write(plaintext)
	edits.close()
	edit("edits.txt")
	edits=open("edits.txt", "r+")
	i=len(edits.read())
	while(i % len(key) != 0):
		edits.write(".")
		i+=1
	i=0
	f.close()
	os.remove(filename)
	f=open(filename, "w")
	edits.seek(0)
	for ch in edits.read():
		f.write(chr( ord(ch)^ord(key[i]) ))
		i+=1
		i=i%len(key)
	edits.close()
	f.close()
	os.remove("edits.txt")
	#upload revised file to google drive?
