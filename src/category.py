

class Category:
    """Класс для предствавления категории"""
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products) if products else 0
        Category.category_count += 1


if __name__ == "__main__":
    category = Category("Спорт", "Спортивные кроссовки", "Бутсы")

    print(category.name)
    print(category.description)
    print(category.products)
    print(category.product_count)
    print(category.category_count)
