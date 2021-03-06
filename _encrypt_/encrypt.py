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

donate_link = "https://bit.ly/3gE7R48" #updated donate link

#encrypt file-folder
def encrypt_func():
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

            #deleting original files
            for f in files:
                #del
                os.remove(original_path+f)
                #done with deleting... 
            else:    
                print(" ")
                print(f"{Back.BLACK}{Fore.GREEN}done! here is your encryption key you´ll need it for decryption[NOTE: if you lose it your file´s are gone!]")
                #print key
                print(f"{Back.BLACK}{Fore.LIGHTCYAN_EX}{key}")
                print(f"donate BTC: {donate_link}")
                #del key
                os.remove("YOUR_KEY_PLS_SAVE.key")
                #wait
                time.sleep(30)
                #del cache
                subprocess.call([r'auto_del_cache.bat'])
                #exit
                exit()

        
        #don't del original files
        else:
            print(f"{Back.BLACK}{Fore.GREEN}done! here is your encryption key you´ll need it for decryption[NOTE: if you lose it your file´s are gone!]")
            #print key
            print(f"{Back.BLACK}{Fore.LIGHTCYAN_EX}{key}")
            print(f"donate BTC: {donate_link}")
            #wait
            time.sleep(5)
            #del key
            os.remove("YOUR_KEY_PLS_SAVE.key")
            #wait
            time.sleep(30)
            #del cache
            subprocess.call([r'auto_del_cache.bat'])
            #exit
            exit()

