class Note:
    def __init__(self, name, surname, date_birth, number):
        self.__name = name
        self.__surname = surname
        self.__date_birth = date_birth
        self.__number = number

        @property
        def name(self):
            return self.__name
        @name.setter
        def name(self, name):
            if not isinstance(name, str):
                raise TypeError()
            self.__name = name

        @property
        def surname(self):
            return self.__name

        @surname.setter
        def surname(self, sname):
            if not isinstance(sname, str):
                raise TypeError()
            self.__surname = sname

    def __str__(self):
        return f'Data:\n{self.__name} {self.__surname} {self.__date_birth} {self.__number}'


class Notebook:

    def __init__(self):
        self.nb = list()

    def __str__(self):
        return f'{self.nb} \n-----'


class Search(Notebook):
    def operation(self, field):
        for item in self.nb:
            if field in item.nb:
                    return item
            raise ValueError("Search:not found.")


class Add(Notebook):
    def operation(self, *classes):
        if not isinstance(classes, Note):
            raise TypeError("Add:wrong type.")
        if not all(note != classes for note in self.nb):
            raise ValueError("Add:This person is already added.")
        self.nb.append(classes)


class Extract(Notebook):
    def operation(self, element):
        if not element in self.nb:
            raise AttributeError("Delete:Not found.")
        self.nb.remove(element)


def action(val, *element):
    val.operation(element)


def main():
    add = Add()
    extract = Extract()
    lookup = Search()
    pupil1 = Note("Alina", "Krut", 3801010101, "24/01/2003")
    pupil2 = Note("Maxym", "Stalychenko", 3801010102, "14/07/2003")
    pupil3 = Note("Sasha", "Rushchuk", 3801010103, "14/08/2003")

    journal = Notebook()
    action(add, pupil1, pupil2, pupil3)
    print(journal)
    action(lookup, "Olha")
    action(extract, pupil2)

if __name__ == "__main__":
    main()