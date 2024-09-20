import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def first_product():
    return Product(
        name = "name",
        description = "description",
        price = "price",
        quantity = "quantity"
    )