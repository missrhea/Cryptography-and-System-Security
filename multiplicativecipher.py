import fractions
import collections

# Resource : http://www.nku.edu/~christensen/section%206%20multiplicative%20ciphers.pdf

def findModInverse(a, m):
    #if gcd(a, m) != 1:
     #   return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


plaintext=raw_input("Enter Plain Text\t")
key=input("Enter key\t")

#check if multiplicative inverse exists
gcd=fractions.gcd(key, 26) 
if gcd == 1 :
   plaintext = plaintext.replace(' ', '')
   ciphertext=""
   for char in plaintext:
   	char= chr( ( ( (  ord(char) -97 ) *key)%26)+97)
	ciphertext=""+ciphertext+""+char+""
		
   print "Cipher Text :  "+ciphertext
   #find multiplicative inverse of key
   modinv=findModInverse(key,26)
   plaintext=""
   for char in ciphertext:
   	char= chr( ( ( (  ord(char) -97 ) *modinv)%26)+97)
	plaintext=""+plaintext+""+char+""
   print "\nPlain Text:  "+plaintext
		

elif gcd!=1 :
     print "The multiplicative cipher for "+str(key)+" does not exist.  Try another key."



'''
# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [23:49:11] 
$ python multiplicativecipher.py
Enter Plain Text	y
Enter key	3
Cipher Text :  u

Plain Text:  y

# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [23:51:36] 
$ python multiplicativecipher.py
Enter Plain Text	rhea
Enter key	3
Cipher Text :  zvma

Plain Text:  rhea

# rhea @ rhea-Lenovo in ~/Documents/gittest/Cryptography-and-System-Security on git:master x [23:51:51] 
$ python multiplicativecipher.py
Enter Plain Text	zvma
Enter key	9
Cipher Text :  rhea

Plain Text:  zvma

'''
