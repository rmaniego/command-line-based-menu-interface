import os
import json
from datetime import datetime
from tabulate import tabulate
    
# Application Configuration
WIDTH = 50
MENU_OPTIONS = {
    "1": "Add Item",
    "2": "Show Inventory",
    "3": "Generate Reports",
    "4": "Backup Data",
    "0": "Exit"
}

def main():
    """
    The main function that displays the App Menu options
    """
    
    while 1:
        print("")
        print("#"*WIDTH)
        print(decorate_text("CLI-based Demo Application v1.0.0", WIDTH, marker="#"))
        print(decorate_text("© Developers 2023", WIDTH, marker="#"))
        print("#"*WIDTH)
        
        print("")
        print(decorate_text("MAIN MENU", WIDTH, padding="#", marker="#", newline="\n"))
        
        # Display the menu
        for key, option in MENU_OPTIONS.items():
            print(f" {key}: {option}")
        
        selected = ""
        while selected not in MENU_OPTIONS:
            selected = input("SELECT: ").strip()
        
        if selected == "0":
            print(decorate_text("Closing the application", WIDTH, padding="#", marker="#", newline="\n"))
            print("x"*WIDTH)
            break
        
        if selected == "1":
            add_new_item()
        elif selected == "2":
            show_inventory()
        elif selected == "3":
            print("\nFeature coming soon...")
        elif selected == "4":
            create_new_backup()

def show_inventory():
    inventory = load_inventory()
    print(decorate_text("ITEMS", WIDTH, padding="#", marker="#", newline="\n"))
    
    if not inventory:
        print(" * No items found.")
        return

    # https://pypi.org/project/tabulate/
    table = tabulate(inventory, headers="keys", tablefmt="grid")
    print(table)

def add_new_item():
    print(decorate_text("New Item", WIDTH, padding="#", marker="#", newline="\n"))
    
    try:
        item = input("Item name:\t").strip()
        price = float(input("Item price:\t").strip())
        amount = float(input("Amount:\t\t").strip())
        unit_of_measure = input("Unit of measure: ").strip()
    except:
        print("-"*WIDTH)
        print("Error: Only enter valid inputs.")
        print("*"*WIDTH)
        return

    save_to_inventory(item, price, amount, unit_of_measure)
    
    print("-"*WIDTH)
    print(f"{item}' was successfully added to inventory.")
    print("*"*WIDTH)

def save_to_inventory(item, price, amount, unit_of_measure):
    
    print(decorate_text("New Item", WIDTH, padding="#", marker="#", newline="\n"))
    inventory = load_inventory()
    
    # append to the inventory
    inventory.append({"item": item, "price": price, "amount": amount, "unit": unit_of_measure})
    
    # update inventory file
    with open("data/inventory.json", "w+") as file:
        json.dump(inventory, file)
    
    print("-"*WIDTH)
    print(f"{item}' was successfully added to inventory.")
    print("*"*WIDTH)

def create_new_backup():

    print(decorate_text("BACKUP", WIDTH, padding="#", marker="#", newline="\n"))
    print("Backing up inventory data...")
    
    inventory = load_inventory()
    
    backup_path = "data/backup"
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

    # Make unique back up filenames
    timestamp = int(datetime.now().timestamp())
    with open(f"{backup_path}/inventory-{timestamp}.json", "w+") as file:
        json.dump(inventory, file)
    
    print("-"*WIDTH)
    print("Successfully performed backup operation.")
    print("*"*WIDTH)

def load_inventory():
    try:
        with open("data/inventory.json", "r") as file:
            return json.load(file)
    except:
        # Return an empty dictionary
        return []

def decorate_text(text, WIDTH, padding=" ", marker="", newline=""):
    decorated_text = f"{marker} {text} "
    if len(decorated_text) >= WIDTH:
        return f"{newline}{decorated_text} {marker}"
    decorated_text = decorated_text.ljust(WIDTH-1, padding)
    return f"{newline}{decorated_text}{marker}"

if __name__ == "__main__":
    main()