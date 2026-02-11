import random
import os
import time

# إعداد الألوان والرموز
green = "\033[1;32m"
reset = "\033[0m"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()"

def matrix_effect():
    # الحصول على حجم شاشة الترمكس
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    
    # مصفوفة لتتبع المواقع
    drops = [0] * columns

    os.system('clear')
    
    try:
        while True:
            line = ""
            for i in range(columns):
                if random.random() > 0.95:
                    char = random.choice(chars)
                    line += f"{green}{char}{reset}"
                else:
                    line += " "
            
            print(line)
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nStopping Matrix...")

if __name__ == "__main__":
    matrix_effect()

