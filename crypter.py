#import module´s
import os
from colorama import init, Fore, Back
init(autoreset=True)
import time
import subprocess
#import de-encrypt python file´s:
from _decrypt_.decrypt import decrypt_func
from _encrypt_.encrypt import encrypt_func
#VERSION OF PROJECT
ver = ("v1.5")


def main():
    try:

        #EMPTY CMD AND CHANGE ITS NAME
        os.system("cls")
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(f"crypter [{ver}]")

        #LOGO AND MAKER
        print (f"""{Back.BLACK}{Fore.LIGHTCYAN_EX}\
 .o88b. d8888b. db    db d8888b. d888888b d88888b d8888b. 
d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' 88'     88  `8D 
8P      88oobY'  `8bd8'  88oodD'    88    88ooooo 88oobY' 
8b      88`8b      88    88~~~      88    88~~~~~ 88`8b   
Y8b  d8 88 `88.    88    88         88    88.     88 `88. 
 `Y88P' 88   YD    YP    88         YP    Y88888P 88   YD """)
        print (f"{Back.BLACK}{Fore.LIGHTRED_EX}{ver}                      [made by; cookie-_-#2131 on dc]")
        print (" ")

        #ASK INPUT
        print (f"{Back.BLACK}{Fore.LIGHTMAGENTA_EX}do you want to decrypt[1] / encrypt[2] your file/folder ?")
        #GET INPUT
        en_decrypt = input("")

        #ENCRYPT
        if en_decrypt == "2":
            print(" ")
            #START ENCRYPTION FUNCTION IN = [ _encrypt_.encrypt ]
            encrypt_func()
        else:
        #DECRYPT
            print(" ")
            #START DECRYPTION FUNCTION IN = [ _decrypt_.decrypt ]
            decrypt_func()
    
    #WHEN DE-ENCRYPTION DONE;
    except:
        #DELETE CACHE
        subprocess.call([r"del-py-cache-bec_it_sucks.bat"])
        time.sleep(2)
        #CLEAR CMD
        os.system("cls")
        #RESTART
        main()



