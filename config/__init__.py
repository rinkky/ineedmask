import os
from ruamel import yaml

def get_all_products():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    products_file = os.path.join(dir_path, 'products.yml')
    with open(products_file) as f:
        product_list = yaml.load(f)
    return product_list
