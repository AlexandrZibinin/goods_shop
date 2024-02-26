from Classes import Category, Product

my_cat = Category('fruit', 'round', [])
# вот продукт
product_data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
product_data2 = {
        "name": "iphone 4g",
        "description": "16GB, Серый цвет, 2MP камера",
        "price": 9800.0,
        "quantity": 1
      }
# пытаемся добавить продукт в категорию
my_new = Product.create_product(product_data)
my_new2 = Product.create_product(product_data2)


my_cat.goods = my_new
my_cat.goods = my_new2


print(my_cat.goods)


# my_cat.get_goods()

