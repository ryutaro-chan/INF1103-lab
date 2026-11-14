import pytest
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount
from product_factory import ProductFactory

def test_no_discount():
    assert NoDiscount().apply(100.0) == 100.0

def test_percentage_discount():
    assert PercentageDiscount(10).apply(200.0) == 180.0

def test_bulk_discount():
    assert BulkDiscount(200, 20).apply(250.0) == 230.0

def test_product_factory_invalid():
    class DummySupplier: pass
    with pytest.raises(ValueError):
        ProductFactory.create("service", "S001", "Test", 30.0, 5, DummySupplier())