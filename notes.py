import os

def note_app():
    file_name = "my_notes.txt"
    
    while True:
        os.system('clear')
        print("=== Note Manager ===")
        print("1. Write a new note")
        print("2. Read saved notes")
        print("3. Delete all notes")
        print("4. Exit")
        
        choice = input("\nChoose (1-4): ")

        if choice == '1':
            note = input("\nEnter your note: ")
            with open(file_name, "a") as f:
                f.write("- " + note + "\n")
            print("\nNote saved successfully!")
            input("Press Enter to continue...")
            
        elif choice == '2':
            print("\n--- Your Saved Notes ---")
            if os.path.exists(file_name):
                with open(file_name, "r") as f:
                    print(f.read())
            else:
                print("No notes found.")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            if os.path.exists(file_name):
                os.remove(file_name)
                print("\nAll notes deleted.")
            else:
                print("\nNothing to delete.")
            input("Press Enter to continue...")
            
        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    note_app()

