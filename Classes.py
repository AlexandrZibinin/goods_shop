class Category:
    name: str
    description: str

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods

    @property
    def goods(self):
        """геттер списка товаров раздела категории"""
        goods = []
        for value in self.__goods:
            st = f"{value.name}, {value.price} руб. Остаток: {value.quantity} шт."
            goods.append(st)
        return goods

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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price) -> float:
        """сеттер стоимости товара с проверкой"""
        if new_price <= 0:
            print('Цена введена некорректная')
            return
        self.__price = new_price

    @classmethod
    def create_product(cls, product_data: dict):
        """создание экземпляра класса с помощью распаковки словаря"""
        return cls(**product_data)
