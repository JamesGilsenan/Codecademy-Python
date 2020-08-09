print("My name is {name} and I'm feeling {feeling}.".format(name="Yon Lad", feeling="Yabadabadoo"))

# Checkpoint 2
from Products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

create_products(Baseball=3, Shirt = 14, Guitar = 70)