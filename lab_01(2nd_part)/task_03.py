class Product:

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.dimension = quantity

        @property
        def price(self):
            return self.__price

        @price.setter
        def price(self, value):
            if not isinstance(value, int | float):
                raise ValueError('Price is not a number.')
            if not value:
                raise ValueError('Price cannot be equal 0.')
            if value < 0:
                raise ValueError('Price cannot be a negative number.')
            self.__price = value

        @price.getter
        def price(self):
            return self.__price

    def __str__(self):
        return f'{self.name}'


class Customer:
    def __init__(self, name, surname, patronymic, mobile):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile = mobile

    def __str__(self):
        return f'{self.name} {self.surname}'


class Order:

    def __init__(self, customer):
        self.cart_items = []
        self.summary = 0.0
        self.customer = customer

    def add_item(self, item_name, item_price, item_quantity):
        for x in range(item_quantity):
            self.cart_items.append(item_name)
            self.summary += item_price

    def summarising(self):
        cart_items = dict((item, self.cart_items.count(item)) for item in self.cart_items)
        return cart_items

    def __str__(self):
        self.products_list = self.summarising()
        return f'{self.customer} bought {self.summarising()}' \
            f'\nIn total: {self.summary}'


def main():
    user1 = Customer('Ternov', 'Stepan', 'Mykhailovych', '53600')
    apple = Product('apple', 3.59, 'tasty', 10)
    pear = Product('apple', 2.99, 'awful', 10)
    order1 = Order(user1)
    order1.add_item(apple, 3.59, 3)
    order1.add_item(pear, 2.99, 1)
    print(order1)


if __name__ == '__main__':
    main()