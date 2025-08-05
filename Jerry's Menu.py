import getpass
import webbrowser

passattempts = 3
password = "Jerry999JustBetter"

print("hello")
name = input("what is your name? ")
if name == "Jerry":
    print("Welcome, Mayor Jerry")
else:
    print("hello, " + name)
    permissionquestion = input("Do you work for Jerry? ")
    if permissionquestion == "yes":
        while passattempts > 0:
            userpass = getpass.getpass("What is the password (3 attempts): ")
            if userpass == password:
                print("Access Granted")
                break
            elif passattempts > 1:
                print("Access Denied")
                passattempts -= 1
                print(f"you have {passattempts} attempts left")
            else:
                print("Too many attemps, closing Program...")
                exit()
    else:
        print("Goodbye")
        exit()

def main_menu():
    print("\n--- Jerry's main Menu ---")
    print("1. Skyblock Menu")
    print("2. Other Menu")
    print("3. Exit")
    print("-----------------")

def Skyblock_menu():
    print("\n--- Jerry's Skyblock Menu ---")
    print("1. Check the Bazzar")
    print("2. Check the Auction House")
    print("3. Main Menu")
    print("-----------------")

def other_menu():
    print("\n--- Jerry's Other Menu ---")
    print("1. Official Minecraft Website")
    print("2. Minecraft Wiki")
    print("3. Popular Minecraft Servers List")
    print("4. Minecraft Mod/Resource Pack Site (CurseForge)")
    print("5. Other Games News")
    print("6. Main Menu") # Updated option number
    print("-----------------")

while True:
    main_menu()
    choice = input("Please select an option (1-3): ")

    if choice == "1":
        while True:
            Skyblock_menu()
            choice = input("Please select an option (1-3): ")
            if choice == "1":
                print("Opening the Bazzar...")
                webbrowser.open("https://unrealmc.ddns.net/WebApps/BZ")
            elif choice == "2":
                print("Opening the Auction House...")
                webbrowser.open("https://unrealmc.ddns.net/WebApps/AH")
            elif choice == "3":
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice, please try again.")

    elif choice == "2":
        print("Opening Other Menu...")
        while True:
            other_menu()
            other_choice = input("Please select an option (1-6): ") # Updated range

            if other_choice == "1":
                print("Opening Official Minecraft Website...")
                webbrowser.open("https://www.minecraft.net/")
            elif other_choice == "2":
                print("Opening Minecraft Wiki...")
                webbrowser.open("https://minecraft.fandom.com/wiki/Minecraft_Wiki")
            elif other_choice == "3":
                print("Opening Popular Minecraft Servers List (e.g., Minecraft-Server.net)...")
                webbrowser.open("https://minecraft-server.net/")
            elif other_choice == "4":
                print("Opening Minecraft Mod/Resource Pack Sites (CurseForge)...")
                webbrowser.open("https://www.curseforge.com/minecraft")
            elif other_choice == "5":
                print("Opening Other Games News (e.g., IGN)...")
                webbrowser.open("https://www.ign.com/games")
            elif other_choice == "6": # Updated option number for Main Menu
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice, please try again.")

    elif choice == "3":
        
        if name == "Jerry":
            print("See you Next time, Jerry!")
        else:
            print("Thank you for helping Mayor Jerry. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        