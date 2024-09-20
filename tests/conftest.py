import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def product():
    return Product(
        name = "name",
        description = "description",
        price = "price",
        quantity = "quantity"
    )

@pytest.fixture
def category():
    return Category(
        name = "name",
        description = "description",
        products = "products",
        # product_count += len(products) if products else 0
        # category_count += 1
    )

@pytest.fixture
def product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, 200MP камера", 180000.0, "5")

@pytest.fixture
def category():
    return Category("Спорт", "Спортивные кроссовки", "Бутсы")