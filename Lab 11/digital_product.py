from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier, file_size: float = 0.0):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.file_size = file_size