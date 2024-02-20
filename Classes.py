class Category:
    name: str
    description: str
    goods: list

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

    def append_goods(self, new_goods):
        """добавление товара из экземпляра Product в список товаров Category"""
        self.goods.append(new_goods.name)

    @property
    def displaying_goods(self, new_goods):
        """вывод информации о товаре"""
        return f'{self.__goods}, {new_goods.price} руб. Остаток: {new_goods.quantity_in_stock} шт.'

class Product:

    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.total_categories = 0
        self.total_unique_products = 0

    @classmethod
    def new_product(cls, new_product):
        """Для класса Product добавить метод, который создает товар и возвращает объект,
        который можно добавлять в список товаров."""
        name, description, price, quantity_in_stock = new_product.split(' ')
        return cls(name, description, price, quantity_in_stock)


    @property
    def get_price(self):
        return self.price

    @get_price.setter
    def get_price(self, new_price):
        self.price = new_price

    def get_info_price(self):
        """если цена ниже или равна 0 выводит сообщение о некорректной цене"""
        if self.get_price() <= 0:
            print('цена введена некорректная')
