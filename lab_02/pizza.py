ingredient = {
    'dough': 0.5,
    'tomato_sauce': 0.35,
    'garlic': 0.25,
    'pepperoni': 0.4,
    'chilli': 0.9,
    'mushrooms': 1.0,
    'bacon': 1.4,
    'salami': 1.0,
    'cheese': 0.6
}


class Pizza:
    def __init__(self):
        self.pizza = __class__.__name__
        self.ingredients = ['dough', 'tomato_sauce']
        self.total = 0

    def add_in(self, *argv):
        for name in argv:
            if not name in ingredient:
                raise Exception('ingredient was not found.')
            self.ingredients.append(name)

    def summarizing(self):
        for i in range(len(self.ingredients)):
            self.total += ingredient.get(self.ingredients[i])
        return self.total


    def __str__(self):
        self.summarizing()
        return f'You are ordering {self.pizza} pizza\ningredients:{self.ingredients}\ntotal:{self.total}€'


class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza = __class__.__name__
        super().add_in('garlic', 'pepperoni')


class Bacon(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza = __class__.__name__
        super().add_in('cheese', 'pepperoni', 'bacon')


class Chili(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza = __class__.__name__
        super().add_in('chilli', 'pepperoni', 'bacon')


class Vegan(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza = __class__.__name__
        super().add_in('cheese', 'pepperoni', 'mushrooms')


class Salami(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza = __class__.__name__
        super().add_in('cheese', 'salami', 'pepperoni')


#pizza = Salami()
#print(pizza)