import os

def calculator():
    while True:
        os.system('clear')
        print("=== Smart Calculator ===")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("\nChoose (1-5): ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("First number: "))
                num2 = float(input("Second number: "))
            except ValueError:
                print("Error! Please enter numbers only.")
                input("Press Enter to continue...")
                continue

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error! Division by zero.")
            
            input("\nPress Enter for another operation...")
        else:
            print("Invalid choice!")
            input("Press Enter to try again...")

if __name__ == "__main__":
    calculator()

