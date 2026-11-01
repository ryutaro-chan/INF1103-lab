from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def main():
    inv = Inventory()
    inv.load_from_json()

    while True:
        print("\n===================================")
        print(" INVENTORY MANAGEMENT SYSTEM (LAB 7)")
        print("===================================")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search product")
        print("5. Save inventory")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == "1":
            inv.display_all()
            
        elif choice == "2":
            p_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            price = float(input("Enter Price ($): "))
            qty = int(input("Enter Stock Quantity: "))
            
            print("\nProduct Types:")
            print(" 1. Physical Product")
            print(" 2. Digital Product")
            p_type = input("Select Product Type (1 or 2): ").strip()
            
            if p_type == "1":
                weight = float(input("Enter Weight in kg: "))
                prod = PhysicalProduct(p_id, name, price, qty, weight)
            else:
                size = float(input("Enter Download Size in MB: "))
                prod = DigitalProduct(p_id, name, price, qty, size)
                
            inv.add_product(prod)
            print(f"Successfully added '{name}' to inventory.")
            
        elif choice == "3":
            p_id = input("Enter Product ID to update: ").strip()
            amt = int(input("Enter stock adjustment (e.g., 5 or -2): "))
            inv.update_stock(p_id, amt)
            
        elif choice == "4":
            p_id = input("Enter Product ID to search: ").strip()
            inv.search_product(p_id)
            
        elif choice == "5":
            inv.save_to_json()
            
        elif choice == "6":
            inv.save_to_json()
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose options 1 through 6.")

if __name__ == "__main__":
    main()