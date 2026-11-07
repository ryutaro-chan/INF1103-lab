from supplier import Supplier
from product import Product, CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, quantity: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, quantity, supplier)
        self.weight: float = weight

   
    def display_information(self) -> None:
        super().display_information()
        print(f"  └─ Type: Physical | Weight: {self.weight} kg | Shipping Fee: ${self.calculate_shipping_cost():.2f}")


    def get_fulfilment_info(self) -> str:
        return f"Physical shipping required for {self.name} (Weight: {self.weight} kg)."

    def calculate_shipping_cost(self) -> float:
        return 5.0 + (self.weight * 2.0)