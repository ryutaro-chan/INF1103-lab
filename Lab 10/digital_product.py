from supplier import Supplier
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity: int, download_size: int, supplier: Supplier):
        super().__init__(product_id, name, price, quantity, supplier)
        self.download_size: int = download_size

  
    def display_information(self) -> None:
        super().display_information()
        print(f"  └─ Type: Digital | Download Size: {self.download_size} MB")

    def get_fulfilment_info(self) -> str:
        return f"Instant digital download provided ({self.download_size} MB)."