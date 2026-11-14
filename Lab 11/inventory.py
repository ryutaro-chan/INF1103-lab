from discount_strategy import DiscountStrategy, NoDiscount

class OrderLine:
    def __init__(self, product, quantity: int):
        # Validation: Order line quantity must be greater than zero[cite: 5]
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


class Order:
    def __init__(self, discount: DiscountStrategy = None):
        self.order_lines = []
        # Defaults to NoDiscount if none is specified[cite: 3]
        self.discount = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        """Allows changing the discount strategy dynamically on an existing order."""
        self.discount = discount

    def add_order_line(self, line: OrderLine) -> None:
        self.order_lines.append(line)

    def calculate_total(self) -> float:
        """Calculates subtotal and passes the result to the strategy's apply method[cite: 3]."""
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)