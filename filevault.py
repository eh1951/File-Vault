import os
from Crypto import Random
from Crypto.Cipher import DES3, AES, DES
from time import time
def main():
				print("Welcome to Evan and Mac's File Vault")
				print("What encryption would you like to use? 1 = DES, 2 = 3DES, 3 = AES")
				number = input ("Enter a number: ")
				directory = input ("Please enter the file location of the folder: ")
				#key2 = input("please enter the location of your key: ")
				if number == '3':
								key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
								for filename in os.listdir(directory):
									if filename.endswith(".txt"):
										encrypt_file("vault/" + filename, key)
										decrypt_file("encrypted/vault/" + filename +".enc", key)
				if number == '1':
								key = b'-8B key-'
								for filename in os.listdir(directory):
									print(filename)
									print(os.path.dirname(filename))
									if filename.endswith(".txt"):
										DES_encrypt_file("vault/" + filename, key)
										DES_decrypt_file("encrypted/vault/" + filename + ".enc", key)
				if number == '2':
								key = b'i like tacos1234'
								for filename in os.listdir(directory):
									if filename.endswith(".txt"):
										DES3_encrypt_file("vault/" + filename, key)
										DES3_decrypt_file(("encrypted/vault/" + filename + ".enc"), key)

def pad(s):
				return (s + b"\0" * (AES.block_size - len(s) % AES.block_size))

def DES_pad(message):
				while len(message) % 8 != 0:
								message += b"\0"
				return message

def encrypt(message, key, key_size=256):
				message = pad(message)
				iv = Random.new().read(AES.block_size)
				cipher = AES.new(key, AES.MODE_CBC, iv)
				return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
				iv = ciphertext[:AES.block_size]
				cipher = AES.new(key, AES.MODE_CBC, iv)
				plaintext = cipher.decrypt(ciphertext[AES.block_size:])
				return plaintext.rstrip(b"\0")
 
def encrypt_file(fileLocation, key):
				with open(fileLocation, 'rb') as fo:
								plaintext = fo.read()
				enc = encrypt(plaintext, key)
				os.makedirs(os.path.dirname("encrypted/" + fileLocation + ".enc"), exist_ok = True)
				with open("encrypted/"+ fileLocation + ".enc", 'wb') as fo:
								fo.write(enc)
				#with open(fileLocation + ".enc", 'wb') as fo:
				#				fo.write(enc)

def decrypt_file(fileLocation, key):
				with open(fileLocation, 'rb') as fo:
								ciphertext = fo.read()
				dec = decrypt(ciphertext, key)
				os.makedirs(os.path.dirname("decrypted/" + fileLocation[:-4]), exist_ok = True)
				with open("decrypted/"+ fileLocation[:-4], 'wb') as fo:
				#with open(fileLocation[:-4], 'wb') as fo:
								fo.write(dec)

def DES_encrypt(message, key):
				des = DES.new(key, DES.MODE_ECB)
				paddedMessage = DES_pad(message)
				DES_enc = des.encrypt(paddedMessage)
				return DES_enc

def DES_decrypt(ciphertext, key):
				des = DES.new(key, DES.MODE_ECB)
				plaintext = des.decrypt(ciphertext)
				return plaintext.rstrip(b"\0")

def DES_encrypt_file(fileLocation, key):
				with open(fileLocation, 'rb') as fo:
								plaintext = fo.read()
				enc = DES_encrypt(plaintext, key)
				os.makedirs(os.path.dirname("encrypted/" + fileLocation + ".enc"), exist_ok = True)
				with open("encrypted/"+ fileLocation + ".enc", 'wb') as fo:
								fo.write(enc)

def DES_decrypt_file(fileLocation, key):
				with open(fileLocation, 'rb') as fo:
					ciphertext = fo.read()
				dec = DES_decrypt(ciphertext, key)
				os.makedirs(os.path.dirname("decrypted/" + fileLocation[:-4]), exist_ok = True)
				with open("decrypted/"+ fileLocation[:-4], 'wb') as fo:
				#with open(fileLocation[:-4], 'wb') as fo:
					fo.write(dec)

def DES3_pad(message):
		return (message + b"\0" * (DES3.block_size - len(message) % DES3.block_size))


def DES3_encrypt(message , key):
				message = DES3_pad(message)
				iv = Random.new().read(DES3.block_size)
				cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
				enc = cipher_encrypt.encrypt(message)
				return iv + enc

def DES3_decrypt(ciphertext, key):
		iv = ciphertext[:DES3.block_size]
		cipher = DES3.new(key,DES3.MODE_OFB, iv)
		plaintext = cipher.decrypt(ciphertext[DES3.block_size:])
		return plaintext.rstrip(b"\0")

def DES3_encrypt_file(fileLocation, key):
		with open(fileLocation, 'rb') as fo:
				plaintext = fo.read()
		enc = DES3_encrypt(plaintext, key)
		os.makedirs(os.path.dirname("encrypted/" + fileLocation + ".enc"), exist_ok = True)
		with open("encrypted/"+ fileLocation + ".enc", 'wb') as fo:
		#with open(fileLocation + ".enc", 'wb') as fo:
				fo.write(enc)

def DES3_decrypt_file(fileLocation, key):
		with open(fileLocation, 'rb') as fo:
				ciphertext = fo.read()
		dec = DES3_decrypt(ciphertext, key)
		os.makedirs(os.path.dirname("decrypted/" + fileLocation[:-4]), exist_ok = True)
		with open("decrypted/"+ fileLocation[:-4], 'wb') as fo:
		#with open(fileLocation[:-4], 'wb') as fo:
				fo.write(dec)
main()

