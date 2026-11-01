from product import Product

# 1.3 DigitalProduct inherits from Product
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity: int, download_size: float):
        # Reuse existing Product constructor using super()
        super().__init__(product_id, name, price, quantity)
        self.download_size = download_size  # Size in megabytes

    # 2.1 Override display_information using super()
    def display_information(self) -> None:
        super().display_information()
        print(f"  └─ Type: Digital | Download Size: {self.download_size} MB")

    # 3.2 Implement get_fulfilment_info
    def get_fulfilment_info(self) -> str:
        return f"Instant digital download provided ({self.download_size} MB)."