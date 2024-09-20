
def test_prod_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == "5"