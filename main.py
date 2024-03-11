from classes import Category, Product, LawnGrass, Smartphone

my_cat = Category('Телефоны', 'без кнопок', [])
# вот продукт
product_data = {
    "name": "Samsung Galaxy",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
    "perfomance": 'test',
    "model": "Galaxy C23 Ultra",
    "value_memory": 256,
    "color": 'black'
}
product_data2 = {
    "name": "iphone 4g",
    "description": "16GB, Серый цвет, 2MP камера",
    "price": 9800.0,
    "quantity": 0
}
# создаем продукт
my_new = Smartphone(**product_data)
# my_new2 = Product.create_product(product_data2)
# # добавляем продукт в категорию
print(repr(my_new))
my_cat.goods = my_new
# my_cat.goods = my_new2

# print(my_new2)
print(my_cat.goods)
# print(my_new + my_new2)

# my_cat.get_goods()

# grass1 = LawnGrass('trava', 'zelenaya', 10.1, 5, 'ru', 5, 'green')
# print(repr(grass1))
# print(Category.average_price(my_cat))
