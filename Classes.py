class Category:
    name: str
    description: str


    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

    def __str__(self):
        for value in self.__goods:
            print(f"{value.name}, {value.price} руб. Остаток: {value.description} шт.")
        return ''

    @property
    def goods(self):
        return self.__goods


    @goods.setter
    def goods(self, new_goods):
        """добавление товара из экземпляра Product в список товаров Category"""
        self.__goods.append(new_goods)

class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_categories = 0
        self.total_unique_products = 0

    @classmethod
    def create_product(cls, product_data: dict):
        """создание экземпляра класса продукта"""
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def check_price(self, new_price) -> float:
        if new_price <= 0:
            return 'Цена введена некорректная'
        self.__price = new_price

