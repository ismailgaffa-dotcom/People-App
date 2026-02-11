import os
import sys

PASSWORD = "6789" 

def login():
    os.system('clear')
    print("\033[1;31m" + "================================")
    print("   SECURE ACCESS - TERMUX LOCK   ")
    print("================================\n" + "\033[0m")
    
    attempt = input("Enter Security Code: ")
    
    if attempt == PASSWORD:
        print("\033[1;32m" + "\nAccess Granted! Welcome Ismail." + "\033[0m")
    else:
        print("\033[1;31m" + "\nWrong Password! Closing Termux..." + "\033[0m")
        os.system('exit')
        sys.exit()

if __name__ == "__main__":
    login()

