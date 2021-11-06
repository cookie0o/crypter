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
def encrypt():
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




#decrypt-file-folder
def decrypt():
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
            print(f"{Back.BLACK}{Fore.RED}the programm is still in beta del encrypted files doesn´t work sry :/")
            print(" ")
            print(f"{Back.BLACK}{Fore.GREEN}done! have fun with your data")
            print("donate: https://www.buymeacoffee.com/cookie0.0")
            #wait
            time.sleep(5)
            print(" ")
            #run main
            main()
        
        #dont del original files
        else:
            print(" ")
            print(f"{Back.BLACK}{Fore.GREEN}done! have fun with your data")
            print("donate: https://www.buymeacoffee.com/cookie0.0")
            #wait
            time.sleep(5)
            print(" ")
            #run main
            main()

def main():
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("crypter [v1.1]")
    #logo-version
    print (f"""{Back.BLACK}{Fore.LIGHTCYAN_EX}\
        .o88b. d8888b. db    db d8888b. d888888b d88888b d8888b. 
        d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' 88'     88  `8D 
        8P      88oobY'  `8bd8'  88oodD'    88    88ooooo 88oobY' 
        8b      88`8b      88    88~~~      88    88~~~~~ 88`8b   
        Y8b  d8 88 `88.    88    88         88    88.     88 `88. 
         `Y88P' 88   YD    YP    88         YP    Y88888P 88   YD """)
    print (f"{Back.BLACK}{Fore.LIGHTRED_EX}v1.1                          [made by; cookie-_-#2131 on dc]")
    print (" ")

    #ask input
    print (f"{Back.BLACK}{Fore.LIGHTMAGENTA_EX}do you want to decrypt[1] / encrypt[2] your file/folder ?")
    #get input
    en_decrypt = input("")
    #process input
    if en_decrypt == "2":
        print(" ")
        encrypt()

    else:
        print(" ")
        decrypt()

main()