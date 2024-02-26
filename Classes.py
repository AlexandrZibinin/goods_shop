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
        return '\n'.join(goods)

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def __len__(self):
        """подсчет количества продуктов в категории"""
        total_goods = len(self.__goods)
        return total_goods

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

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.__len__()} шт.'

    def __len__(self):
        """возвращает количество продукта на складе"""
        return self.quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price) -> float:
        """сеттер стоимости товара с проверкой"""
        if new_price <= 0:
            return 'Цена введена некорректная'
        self.__price = new_price

    @classmethod
    def create_product(cls, product_data: dict):
        """создание экземпляра класса с помощью распаковки словаря"""
        return cls(**product_data)

    def __add__(self, other):
        """возможность складывать объекты между собой таким образом, чтобы результат выполнения сложения двух продуктов
         был сложением сумм, умноженных на количество на складе."""
        return self.__price * self.quantity + other.price * other.quantity