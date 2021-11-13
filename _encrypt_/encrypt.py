import os
from colorama import init, Fore, Back
init(autoreset=True)
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import stdiomask
import random
import string
import subprocess
import glob
import os.path


#encrypt file-folder
def encrypt_func():
    try:
        #ask original path
        print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}pls enter the path of the file/folder you want to encrypt [the imp path needs to end with \]:")
        #get original path input
        original_path = input("path: ")
        #ask output path
        print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}pls enter the output path for the encrypted file´s [the out path needs to end with \]:")
        #get output path encrypted files
        output_path = input("path: ")
        #ask original files deleted
        print(" ")
        print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}do you want your original file´s deleted[yes][no]")
        #get input original files deleted
        original_files_deleted = input("=?: ")
        print(" ")
        #
        #gen key
        key = Fernet.generate_key()
        with open(f'YOUR_KEY_PLS_SAVE.key', 'wb') as mykey:
            mykey.write(key)
        #load key
        with open(f'YOUR_KEY_PLS_SAVE.key', 'rb') as mykey:
            key = mykey.read()
        
        #load key into project 
        k = Fernet(key)

        #start encryption
        files = os.listdir(original_path)
        for f in files:
            #read
            with open(original_path + f, 'rb') as original_file:
                original = original_file.read()
            #encrypt
            encrypted = k.encrypt(original)
            
            #write to output path
            with open (output_path + f + "-crypter", 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

        #done with encryption
        else:
            #read key
            with open('YOUR_KEY_PLS_SAVE.key') as f:
                out_key = f.readlines()
            
            #del original files (under work)
            if original_files_deleted == "yes":
                print(f"{Back.BLACK}{Fore.RED}the programm is still in beta del original files doesn´t work sry :/")
                print(" ")
                print(f"{Back.BLACK}{Fore.GREEN}done! here is your encryption key you´ll need it for decryption[NOTE: if you lose it your file´s are gone!]")
                print(f"{Back.BLACK}{Fore.GREEN}  ⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓ ")
                #print key
                print(f"{Back.BLACK}{Fore.LIGHTCYAN_EX}{key}")
                print("donate: https://www.buymeacoffee.com/cookie0.0")
                #wait
                time.sleep(30)
                #del key
                os.remove("YOUR_KEY_PLS_SAVE.key")
                print(" ")
                #exit
                exit()
            
            #dont del original files
            else:
                print(f"{Back.BLACK}{Fore.GREEN}done! here is your encryption key you´ll need it for decryption[NOTE: if you lose it your file´s are gone!]")
                print(f"{Back.BLACK}{Fore.GREEN}  ⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓⇓ ")
                #print key
                print(f"{Back.BLACK}{Fore.LIGHTCYAN_EX}{out_key}")
                print("donate: https://www.buymeacoffee.com/cookie0.0")
                #wait
                time.sleep(5)
                #del key
                os.remove("YOUR_KEY_PLS_SAVE.key")
                print(" ")
                #exit
                exit()
    except:
        print(f"{Back.BLACK}{Fore.RED}[ERROR] pls restart the programm!")