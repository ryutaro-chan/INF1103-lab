from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class ProductFactory:
    """Factory class to centralise product creation and avoid direct instantiation coupling."""

    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, stock_quantity: int, supplier):
        p_type = product_type.strip().lower()
        
        if p_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier)
        elif p_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")