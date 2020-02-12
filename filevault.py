#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filevault.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os

from Crypto import Random

from Crypto.Cipher import DES3, AES, DES

from time import time

 

def main():

                print("Welcome to Evan and Mac's File Vault")

                print("What encryption would you like to use? 1 = DES, 2 = 3DES, 3 = AES")

                number = input ("Enter a number: ")

                fileLocation = input("Please enter the file location of the folder: ")

                #key2 = input("please enter the location of your key: ")

                if number == '3':

                                key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

                                encrypt_file(fileLocation, key)

                                decrypt_file(fileLocation +".enc", key)

                if number == '1':

                                key = b'-8B key-'

                                DES_encrypt_file(fileLocation, key)

                                DES_decrypt_file(fileLocation + ".enc", key)

                if number == '3'

                                key = 'i like tacos1234'

                                3DES_encrypt_file(fileLocation, key)

                                3DES_decrypt_file(fileLocation + ".enc", key)

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

                with open(fileLocation + ".enc", 'wb') as fo:

                                fo.write(enc)

 

def decrypt_file(fileLocation, key):

                with open(fileLocation, 'rb') as fo:

                                ciphertext = fo.read()

                dec = decrypt(ciphertext, key)

                with open(fileLocation[:-4], 'wb') as fo:

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

                with open(fileLocation + ".enc", 'wb') as fo:

                                fo.write(enc)

 

def DES_decrypt_file(fileLocation, key):

                with open(fileLocation, 'rb') as fo:

                                ciphertext = fo.read()

                dec = DES_decrypt(ciphertext, key)

                with open(fileLocation[:-4], 'wb') as fo:

                                fo.write(dec)

 

def 3DES_pad(message):

                return (message + b"\0" * (DES3.block_size - len(message) % DES3.block_size))

 

def 3DES_encrypt(message , key):

                message = 3DES_pad(message)

                iv = Random.new().read(DES3.block_size)

                ciper_encrypt = DES3.new(key, DES3.Mode_OFB, iv)

                enc = ciper_encrypt.encrypt(message)

                return iv + enc

 

def 3DES_decrypt(ciphertext, key):

                iv = ciphertext[:DES3.block_size]

                cipher = DES3.new(key,DES3.Mode_OFB, iv)

                plaintext = cipher.decrypt(ciphertext[DES3.block_size:])

                return plaintext.rstrip(b"\0")

 

def 3DES_encrypt_file(fileLocation, key):

                with open(fileLocation, 'rb') as fo:

                                plaintext = fo.read()

                enc = 3DES_encrypt(plaintext, key)

                with open(fileLocation + ".enc", 'wb') as fo:

                                fo.write(enc)

 

def 3DES_decrypt_file(fileLocation, key):

                with open(fileLocation, 'rb') as fo:

                                ciphertext = fo.read()

                dec = 3DES_decrypt(ciphertext, key)

                with open(fileLocation[:-4], 'wb') as fo:

                                fo.write(dec)

 

main()
