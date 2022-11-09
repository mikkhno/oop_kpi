#create dictionary (done)

#Extra: Cheese 0.90, Pieces of Chicken Meat 1.20, Pepper 0.70, Tomatoes 0.60, Mushrooms 1.00

#Today is :
#pizza-of-the-day(price):
#would you like to order? 1 - yes 0 - no(done)
#how much? n
#would you like to add something in n-pizza? 1 - yes 0 - no - 2 continue ordering without adding at all
#what do you want to add? Ex.: 1 - cheese + 2 - pepper or 0 - nothing
#okay, here's your order:
#sn
#date, time
#pizza and amount
#spec. pizza and amount
#total
#would you like to pay with cash or by card? 0 - cash 1 - card
#Thanks for ordering, bye-bye!

#main - > pizza of the day -> order -> receipt

order = {}
# class Order:
#     def __init__(self, amount):
#         self.amount = amount
#
#
#     def add_item(self):
#     #name_order
#     #price
#     #extra.add
#
#     def __str__(self):
#         pass



from datetime import datetime
import pizza

p = pizza.Pizza()
print(p.summarizing())
pizza_of_the_day = {
    "Monday": "Margherita",
    "Tuesday": "Bacon",
    "Wednesday": "Chili",
    "Thursday": "Vegan",
    "Friday": "Salami"
}

dt = datetime.now()
today = dt.strftime('%A')
today_pizza = pizza_of_the_day.get(today)
pizza_link = getattr(pizza, today_pizza)
print(getattr(pizza_link,'summarizing'))


def offer():
    print("Hello. Today is",today,",\nand it means that Pizza-of-day is", today_pizza, "pizza!")
    print("Special price for today:", pizza_link, "€")


def order():
    choice = int(input("Would you like to order? 1 - yes, 0 - no\n"))
    if not choice:
        print("Come back later. Bye-bye!")
        return 0
    amount = int(input("How much?\n"))
    if amount <= 0:
        raise Exception('Entered amount cannot be equal or lower than 0')




def main():
    offer()
    order()

if __name__ == "__main__":
    main()