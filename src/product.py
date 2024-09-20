class Product:
    """Класс для представления продукта"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("Samsung Galaxy S23 Ultra", "256GB, 200MP камера", 180000.0, "5")
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
