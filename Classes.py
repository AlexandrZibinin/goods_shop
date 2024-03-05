from abc import ABC, abstractmethod

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

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.__len__()} шт.'

    def __len__(self):
        """подсчет количества продуктов в категории"""
        total_goods = len(self.__goods)
        return total_goods

    @goods.setter
    def goods(self, new_goods):
        """добавление товара из экземпляра Product в список товаров Category"""
        if issubclass(new_goods.__class__, Product) and isinstance(type(new_goods), Product):
            self.__goods.append(new_goods)
        else:
            return f'Товар не является экземпляром класса'


class Mixinclass:

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        '''Method repr для вывода сообщения в виде клаcса и его атрибутов'''
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"Создан объект со свойствами: {object_attributes.strip(',')})"



class ABCproduct:

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def create_product(self):
        pass


class Product(ABCproduct, Mixinclass):

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
            print('Цена введена некорректная')
            return
        self.__price = new_price

    @classmethod
    def create_product(cls, product_data: dict):
        """создание экземпляра класса с помощью распаковки словаря"""
        return cls(**product_data)

    def __add__(self, other):
        """возможность складывать объекты между собой таким образом, чтобы результат выполнения сложения двух продуктов
         был сложением сумм, умноженных на количество на складе."""
        if isinstance(other, type(self)):
            return self.__price * self.quantity + other.price * other.quantity
        else:
            raise ValueError('Ошибка типа, продукты должны быть из одного класса')

class Smartphone(Product, Mixinclass):
    def __init__(self, name, description, price, quantity, perfomance, model, value_memory, color):
        super().__init__(name, description, price, quantity)
        self.perfomance = perfomance
        self.model = model
        self.value_memory = value_memory
        self.color = color

class LawnGrass(Product, Mixinclass):
    def __init__(self, name, description, price, quantity, manufacturer, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        self.color = color

