from abc import ABC, abstractmethod

# 4.1 Create a CanBeShipped interface
class CanBeShipped(ABC):
    """Interface contract for items that can be shipped."""
    
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        """Calculates shipping cost based on specific subclass criteria."""
        pass


# 3.1 Convert Product into an abstract class
class Product(ABC):
    """Abstract base class for all products."""
    
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_stock(self, amount: int) -> None:
        """Updates product stock levels."""
        self.quantity += amount

    # 2.1 Parent implementation of display_information
    def display_information(self) -> None:
        """Displays common product information."""
        print(f"[{self.product_id}] {self.name} | Price: ${self.price:.2f} | Stock: {self.quantity}")

    # 3.1 Define abstract method get_fulfilment_info
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Must be implemented by child classes to return delivery details."""
        pass