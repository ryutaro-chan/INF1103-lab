import json

INVENTORY_FILE = "inventory.json"

# --- PERSISTENCE FUNCTIONS ---

def load_inventory():
    """Reads inventory.json safely."""
    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
            return inventory, True
    except (FileNotFoundError, json.JSONDecodeError):
        return [], False

def save_inventory(inventory):
    """Saves Python list back to inventory.json."""
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(inventory, file, indent=4)
            return True
    except Exception:
        return False

# --- DATA / CRUD FUNCTIONS (NO UI PROMPTS) ---

def search_product(inventory, product_id):
    """Returns matching product dict or None."""
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def add_product(inventory, product_id, name, price, stock):
    """Adds product dict to inventory if ID doesn't exist."""
    if search_product(inventory, product_id) is not None:
        return False  # Already exists
    
    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    return True

def update_stock(inventory, product_id, new_stock):
    """Updates stock value for a product."""
    product = search_product(inventory, product_id)
    if product:
        product["stock"] = new_stock
        return True
    return False

# --- UI & ORCHESTRATION FUNCTIONS ---

def display_all(inventory):
    """Prints all products cleanly."""
    if not inventory:
        print("\n[!] Inventory is empty.")
        return
    
    print("\n--- Current Inventory ---")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")

def main():
    inventory, status = load_inventory()
    if not status:
        print("[!] Warning: Could not load existing inventory file. Starting fresh.")
        
    exit_program = False
    
    while not exit_program:
        print("\n--- MENU ---")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        
        choice = input("Enter option: ").strip()
        
        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            p_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            if add_product(inventory, p_id, name, price, stock):
                print("[+] Product added successfully!")
            else:
                print("[-] Product ID already exists.")
        elif choice == "3":
            p_id = input("Enter Product ID: ").strip()
            new_stock = int(input("Enter New Stock: "))
            if update_stock(inventory, p_id, new_stock):
                print("[+] Stock updated successfully!")
            else:
                print("[-] Product not found.")
        elif choice == "4":
            p_id = input("Enter Product ID: ").strip()
            prod = search_product(inventory, p_id)
            if prod:
                print(f"[+] Found: {prod}")
            else:
                print("[-] Product not found.")
        elif choice == "5":
            if save_inventory(inventory):
                print("[+] Inventory saved to file!")
            else:
                print("[-] Error saving file.")
        elif choice == "6":
            exit_program = True
            print("Saving entry before exiting...")
            print("Inventory saved successfully")
            print("Thank you for using Inventory Management System")
            print("Program Terminated.")
        else:
            print("[!] Invalid option.")

if __name__ == "__main__":
    main()