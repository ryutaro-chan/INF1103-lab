from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Abstract base class for all order discount strategies."""
    
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    """Standard strategy where no discount is applied."""
    
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    """Applies a percentage-based discount (e.g., 10% off)."""
    
    def __init__(self, percentage: float):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)

class BulkDiscount(DiscountStrategy):
    """Applies a fixed deduction if the total meets or exceeds a threshold."""
    
    def __init__(self, threshold: float, discount_amount: float):
        self.threshold = threshold
        self.discount_amount = discount_amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return max(0.0, total - self.discount_amount)
        return total

class StudentDiscount(DiscountStrategy):
    """Custom 4th strategy: Flat $5 student discount for SIT students."""
    
    def __init__(self, discount_value: float = 5.0):
        self.discount_value = discount_value

    def apply(self, total: float) -> float:
        return max(0.0, total - self.discount_value)