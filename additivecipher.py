import collections
import string
import re

#print ord('a')

plaintext = raw_input("enter plain text\n")

key = input("enter key\n")

plaintext = plaintext.replace(' ', '')
ciphertext=""

for char in plaintext:
	char=chr( ( ( (ord(char)+key)-97)%26 ) + 97)
	ciphertext=""+ciphertext+""+char+""

print "\nCipher text :  "+ciphertext

plaintext=""
for char in ciphertext:
	char=chr( (  ( (ord(char)-key)-97)%26 ) + 97  )
	plaintext=""+plaintext+""+char+""

print "\nDecrypted text is:  "+plaintext


'''
# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [18:53:39] 
$ python additivecipher.py
enter plain text
rhea
enter key
2

Cipher text :  tjgc

Decrypted text is:  rhea

# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [18:53:45] 
$ 

# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [18:53:49] 
$ python additivecipher.py
enter plain text
this is python
enter key
1

Cipher text :  uijtjtqzuipo

Decrypted text is:  thisispython

# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [18:53:58] 
$ 
'''
