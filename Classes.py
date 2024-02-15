class Category:
    name: str
    description: str
    goods: str
    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods


class Product:

    def __init__(self, name, description, price: float, quantity_in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.total_categories = 0
        self.total_unique_products = 0
