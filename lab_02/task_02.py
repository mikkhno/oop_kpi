from datetime import datetime
from datetime import date
import pizza

# main order list
order_list = {}

# dictionary for every day
pizza_of_the_day = {
    "Monday": "Margherita",
    "Tuesday": "Bacon",
    "Wednesday": "Chili",
    "Thursday": "Vegan",
    "Friday": "Salami"
}

# selecting the right class
dt = datetime.now()
today = dt.strftime('%A')
today_pizza = pizza_of_the_day.get(today)
pizza_linked = getattr(pizza, today_pizza)()


# creating info for receipt
class Order:

    def __str__(self):
        self.val = 0

    def add_item(self, n, extra):
        order_list.update({n: extra})

    def total_sum(self, value):
        self.val += value

    def total(self):
        return self.val


# creating order
receipt1 = Order()


# what is good for today
def offer():
    print("Hello. Today is", today, ",\nand it means that Pizza-of-day is", today_pizza, "pizza!")
    print("Special offer for you:\n", pizza_linked)


def order():
    choice = int(input("Would you like to order? 1 - yes, 0 - no\n"))
    if not choice:
        print("Come back later. Bye-bye!")
        return 0
    amount = int(input("How much?\n"))
    if amount <= 0:
        raise Exception('Entered amount cannot be equal or lower than 0')

    for n in range(amount):
        print("Would you like to add something in pizza", n + 1, "?   1 - yes  0 - no")
        choice = int(input())
        # if order contains other wishes
        if not choice:
            receipt1.add_item(n, None)
        # if it really does
        if choice:
            # plenty of offering extras
            for i in range(len(pizza.ingredient)):
                print('|', list(pizza.ingredient.keys())[i], list(pizza.ingredient.values())[i], "€", '|', end=" ")
            list_adding = input("\nPlease, write adding ingredients using comma:\n")
            receipt1.add_item(n, list_adding)
            add_array = list_adding.split(", ")
            print(add_array)
            # summing new extras
            for extra in range(len(add_array)):
                pizza_linked.add_in(add_array[extra])
                receipt1.total_sum(pizza_linked.summarizing())


# creating an unique serial number of reciept
def sgen():
    now = datetime.now()
    current_time = now.strftime("%HX%MX%S")
    today = date.today()
    d1 = today.strftime("%dD%mD%Y")
    sn = f'RPTF{d1}F{current_time}'
    return sn


# displaying the receipt
def receipt():
    print("----- R E C E I P T -----")
    print("ReceiptId:", sgen())
    for i in range(len(order_list)):
        print(" x1 ", today_pizza, "pizza\n+", list(order_list.values())[i])

    print("\nTotal: ", receipt1.total, "€")
    print("Thanks for ordering, bye-bye!")


def main():
    offer()
    order()
    receipt()


if __name__ == "__main__":
    main()
