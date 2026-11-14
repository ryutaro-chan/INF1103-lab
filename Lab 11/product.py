class Product:
    def __init__(self, product_id: str, name: str, price: float, stock_quantity: int, supplier):
        # Validation: Price must be greater than zero, stock cannot be negative
        if price <= 0:
            raise ValueError("Product price must be greater than zero.")
        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
            
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.stock_quantity = int(stock_quantity)
        self.supplier = supplier