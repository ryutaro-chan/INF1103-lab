from product import Product, CanBeShipped

# 1.2 & 4.2 PhysicalProduct inherits from Product and implements CanBeShipped
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, quantity: int, weight: float):
        # Reuse existing Product constructor using super()
        super().__init__(product_id, name, price, quantity)
        self.weight = weight  # Weight in kilograms

    # 2.1 Override display_information using super()
    def display_information(self) -> None:
        super().display_information()
        print(f"  └─ Type: Physical | Weight: {self.weight} kg | Shipping Fee: ${self.calculate_shipping_cost():.2f}")

    # 3.2 Implement get_fulfilment_info
    def get_fulfilment_info(self) -> str:
        return f"Physical shipping required for {self.name} (Weight: {self.weight} kg)."

    # 4.2 Implement calculate_shipping_cost ($5 flat fee + $2 per kg)
    def calculate_shipping_cost(self) -> float:
        return 5.0 + (self.weight * 2.0)