import os
from colorama import init, Fore, Back
init(autoreset=True)
import time
#import de-encrypt python file´s:
from _decrypt_.decrypt import decrypt_func
from _encrypt_.encrypt import encrypt_func




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
        #encrypt-file-folder
        encrypt_func()

    else:
        print(" ")
        #decrypt-file-folder
        decrypt_func()

main()