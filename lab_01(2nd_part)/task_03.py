separator = '----------------'

class Product:

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.dimension = quantity

        @property
        def price(self):
            return self.__price

        # checking all the criteria for the price
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
        return f'{self.name} : {self.description}' \
               f'\nonly for {self.price}'


class Customer:
    def __init__(self, name, surname, patronymic, mobile):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile = mobile

    # giving back from a class as a string with data
    def __str__(self):
        return f'{self.name} {self.surname}'


class Order:

    def __init__(self, customer):
        self.cart_items = []
        self.summary = 0.0
        self.customer = customer

    # adding products to order
    def add_item(self, item_name, item_price, item_quantity):
        for x in range(item_quantity):
            self.cart_items.append(item_name)
            self.summary += item_price

    # summarising the list
    def summarising(self):
        cart_items = dict((item, self.cart_items.count(item)) for item in self.cart_items)
        return cart_items

    # displaying all important information
    def __str__(self):
        self.products_list = self.summarising()
        return f'{self.customer} bought {self.summarising()}' \
               f'\nIn total: {self.summary}'


def main():
    apple = Product('apple', 3.59, 'tasty', 10)
    pear = Product('pear', 2.99, 'awful', 10)
    print('Welcome to the shop! Here are what we can offer to you:')
    print(apple)
    print(separator)
    print(pear)
    print(separator)
    user1 = Customer('Ternov', 'Stepan', 'Mykhailovych', '38012345678')
    order1 = Order(user1)
    order1.add_item('apple', 3.59, 3)
    order1.add_item('pear', 2.99, 1)
    print(order1)
    print(separator)
    user2 = Customer('Honcharova', 'Svitlana', 'Maksymivna', '38087654332')
    order2 = Order(user2)
    order2.add_item('pear', 2.99, 7)
    order2.add_item('apple', 3.59, 2)
    print(order2)
    print(separator)


if __name__ == '__main__':
    main()
