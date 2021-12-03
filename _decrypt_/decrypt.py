import os
from colorama import init, Fore, Back
init(autoreset=True)
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
#import stdiomask
import random
import string
import subprocess
import glob
import os.path


#decrypt-file-folder
def decrypt_func():

    #ask encrypted path
    print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}pls enter the path of the file/folder you want to decrypt [the imp path needs to end with \]:")
    #get encrypted path input
    encrypted_files_path = input("path: ")
    #ask output path
    print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}pls enter the output path for the decrypted file´s [the out path needs to end with \]:")
    #get output path decrypted files
    decrypted_out_path = input("path: ")
    #ask encrypted files deleted
    print(" ")
    print (f"{Back.BLACK}{Fore.LIGHTGREEN_EX}do you want your encrypted file´s deleted[yes][no]")
    #get input original files deleted
    encrypted_files_deleted = input("=?: ")
    print(" ")
    #ask key
    print (f"{Back.BLACK}{Fore.RED}pls enter the key you got when you encrypted your file/folder")
    #get key input
    key_imp = input("key: ")

    #load key
    k = Fernet(key_imp)

    #start decryption
    files = os.listdir(encrypted_files_path)
    for f in files:
        #del -crypter
        F = f.replace("-crypter", " ")
        #read
        with open(encrypted_files_path + f, 'rb') as encrypted_data1:
            encrypted_data = encrypted_data1.read()
        #encrypt
        decrypted_data = k.decrypt(encrypted_data)
        
        #write to output path
        with open (decrypted_out_path + F, 'wb') as decrypted_data1:
            decrypted_data1.write(decrypted_data)
    
    #done with encryption
    else:
        #del original files (under work)
        if  encrypted_files_deleted == "yes":

            #deleting original files
            for f in files:
                #del
                os.remove(encrypted_files_path+f)
                #done with deleting... 
            else:
                print(" ")
                print(f"{Back.BLACK}{Fore.GREEN}done! have fun with your data")
                print("donate BTC: https://bit.ly/3D5gxcB")
                #wait
                time.sleep(10)
                #del cache
                subprocess.call([r'auto_del_cache.bat'])
                os.system("cls")
                time.sleep(0.1)
                
        
        #dont del original files
        else:
            print(" ")
            print(f"{Back.BLACK}{Fore.GREEN}done! have fun with your data")
            print("donate BTC: https://bit.ly/3D5gxcB")
            #wait
            time.sleep(10)
            #del cache
            subprocess.call([r'auto_del_cache.bat'])
            os.system("cls")
            time.sleep(0.1)

            