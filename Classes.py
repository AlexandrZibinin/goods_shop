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

    # @goods.getter
    # def get_goods(self):
    #     """вывод информации о товаре"""
    #     for value in self.__goods:
    #         print(f"{value[0]}, {value[2]} руб. Остаток: {value[3]} шт.")

    @goods.setter
    def goods(self, new_goods):
        """добавление товара из экземпляра Product в список товаров Category"""
        self.__goods.append(new_goods)

class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.total_categories = 0
        self.total_unique_products = 0

    @classmethod
    def create_product(cls, product_data: dict):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        return cls(name, description, price, quantity)


    # def new_product(cls, new_product):
    #     """Для класса Product добавить метод, который создает товар и возвращает объект,
    #     который можно добавлять в список товаров."""
    #     name, description, price, quantity = new_product.split(' ')
    #     return cls(name, description, price, quantity)
    #
    #
    #
    # def get_price(self):
    #     return self.price
    #
    #
    # def get_price(self, new_price):
    #     self.price = new_price
    #
    # def get_info_price(self):
    #     """если цена ниже или равна 0 выводит сообщение о некорректной цене"""
    #     if self.get_price() <= 0:
    #         print('цена введена некорректная')
    #
    # def create_product(self):
    #     return [self.name, self.__price, self.quantity]