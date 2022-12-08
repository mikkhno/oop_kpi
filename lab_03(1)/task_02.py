class Notebook:
    def __init__(self):
        self.name = None
        self.surname = None
        self.mobil = 0
        self.birth = "01/01/1990"

    def create(self):
        self.name = str(input("What's the name? "))
        self.surname = str(input("What's the surname? "))
        self.mobil = int(input("What's the mobil?(without +) "))
        self.birth = str(input("What's the birth date? "))

    def __str__(self):
        print(self.__init__)


class Add(Notebook):
    def operation(self, element):
        setattr(Notebook, element, lambda :str(input("value:")))


class Search(Notebook):
    def operation(self, element):
        try:
            print("Value of {} is {}".format(element, getattr(Notebook, element)))
        except:
            raise AttributeError("Search:Not found.")


class Extract(Notebook):
    def operation(self, element):
        try:
            delattr(Notebook, element)
        except:
            raise AttributeError("Delete:Not found.")


def action(val,element):
    val.operation(element)


def main():
    note = Notebook()
    add = Add()
    extract = Extract()
    search = Search()
    note.create()
    choice = input("What do you want to do? (add, extract, search) : ")
    element = input("Which element? ")
    action(choice, element)

