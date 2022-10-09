class Product:

    def __init__(self, price, description, quantity):
        self.price = price
        self.description = description
        self.dimension = quantity


class Customer:
    def __init__(self, name, surname, patronymic, mobile):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile = mobile


class Order:

    def __init__(self, customer, products_list):
        self.cart_items = []
        self.summary = 0.0
        self.customer = customer
        self.products_list = products_list

    def add_item(self, item_name, item_price, item_quantity):
        for x in item_quantity:
            self.cart_items.append(item_name)
            self.summary += item_price

    def summarising(self):
        shop_list = dict((item, self.cart_items.count(item)) for item in self.cart_items)
        return shop_list


def main():
    user1 = Customer('Ternov', 'Stepan', 'Mykhailovych', '53600')
    apple = Product(3.59, 'tasty', 10)
    pear = Product(2.99, 'awful', 10)
    user1_order = Order(user1, products_list='')
    user1_order.add_item(apple, 3.59, 3)
    user1_order.add_item(pear, 2.99, 1)
    user1_order.products_list = user1_order.summarising()
    print(user1_order.products_list)
    print('Total: ', user1_order.summary)

    if __name__ == '__main__':
        main()
