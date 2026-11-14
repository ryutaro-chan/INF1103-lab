from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier, weight: float = 0.0):
        super().__init__(product_id, name, price, stock_quantity, supplier)
        self.weight = weight