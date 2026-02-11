import requests
import os

def get_weather():
    os.system('clear')
    print("=== Global Weather Explorer ===")
    city = input("\nEnter city name (e.g., Tangier, Cairo, Riyadh): ")
    
    # استخدام خدمة wttr.in المجانية والمفتوحة
    url = f"https://wttr.in/{city}?format=3"
    
    try:
        print("\nSearching for weather info...\n")
        response = requests.get(url)
        if response.status_code == 200:
            print("-------------------------------")
            print(response.text)
            print("-------------------------------")
        else:
            print("City not found. Please check the spelling.")
    except:
        print("Network error! Check your internet connection.")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    get_weather()

