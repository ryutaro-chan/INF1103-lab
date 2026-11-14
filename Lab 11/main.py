import csv
from product_factory import ProductFactory

def get_positive_float(prompt: str) -> float:
    """Helper function to handle user input errors and ensure positive numbers[cite: 5]."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def load_products(path: str, inventory, supplier) -> None:
    """Loads products from a CSV file using try/except/else/finally blocks[cite: 6]."""
    loaded = 0
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header row
            
            for row_idx, row in enumerate(reader, start=2):
                if not row or len(row) < 5:
                    continue
                
                p_type, p_id, name, price_str, stock_str = [col.strip() for col in row[:5]]
                
                try:
                    price = float(price_str)
                    stock = int(stock_str)
                    
                    # Create product through the factory instead of directly[cite: 4]
                    product = ProductFactory.create(p_type, p_id, name, price, stock, supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Error on row {row_idx} ({name}): {e}. Skipping row.")
            
            print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")