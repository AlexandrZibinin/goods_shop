from Classes import Category, Product

my_cat = Category('fruit', 'round', [Product('груша', 'красная', 110.0, 5)])
# вот продукт
product_data = {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }
# пытаемся добавить продукт в категорию
my_new = Product.create_product(product_data)

my_cat.goods = my_new

print(my_cat)


# my_cat.get_goods()

