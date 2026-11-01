import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary mapping product_id -> Product object

    def add_product(self, product):
        self.products[product.product_id] = product

    def display_all(self):
        if not self.products:
            print("\nInventory is currently empty.")
            return
        print("\n--- Current Inventory ---")
        for product in self.products.values():
            product.display_information()
            print(f"     Fulfilment: {product.get_fulfilment_info()}")

    def update_stock(self, product_id: str, amount: int):
        if product_id in self.products:
            self.products[product_id].update_stock(amount)
            print("Stock updated successfully.")
        else:
            print("Product not found.")

    def search_product(self, product_id: str):
        product = self.products.get(product_id)
        if product:
            print("\n--- Product Details ---")
            product.display_information()
            print(f"     Fulfilment: {product.get_fulfilment_info()}")
        else:
            print("Product not found.")

    # 5. Save product data to JSON including type details
    def save_to_json(self, filepath: str = "inventory.json"):
        data = []
        for p in self.products.values():
            item = {
                "product_id": p.product_id,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity
            }
            if isinstance(p, PhysicalProduct):
                item["type"] = "physical"
                item["weight"] = p.weight
            elif isinstance(p, DigitalProduct):
                item["type"] = "digital"
                item["download_size"] = p.download_size
            data.append(item)
            
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print("Inventory successfully saved to JSON.")

    # 5. Load product data from JSON and recreate correct subclass instances
    def load_from_json(self, filepath: str = "inventory.json"):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                self.products.clear()
                for item in data:
                    p_type = item.get("type")
                    if p_type == "physical":
                        prod = PhysicalProduct(
                            item["product_id"], item["name"], item["price"], item["quantity"], item["weight"]
                        )
                    elif p_type == "digital":
                        prod = DigitalProduct(
                            item["product_id"], item["name"], item["price"], item["quantity"], item["download_size"]
                        )
                    else:
                        continue
                    self.products[prod.product_id] = prod
            print("Inventory successfully loaded from JSON.")
        except FileNotFoundError:
            print("No saved inventory file found. Starting with fresh inventory.")