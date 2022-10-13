class Student:

    def __init__(self, name, surname, group, rec_book, grades):
        self.name = name
        self.surname = surname
        self.rec_book = rec_book
        self.grades = grades
        self.group = group

    @property
    def rec_book(self):
        return self.__rec_book

    @rec_book.setter
    def rec_book(self, number):
        if not isinstance(number, int):
            raise TypeError('Wrong number of the record book.')

        self.__rec_book = number

    @rec_book.getter
    def rec_book(self):
        return self.__rec_book

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grade_list):
        for grade in grade_list:
            if not isinstance(grade, int):
                raise ValueError('One of the grades was set incorrectly.')
            self.__grades = grade_list

    @grades.getter
    def grades(self):
        return self.__grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.getter
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @surname.getter
    def surname(self):
        return self.__surname

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'| {self.name} | {self.surname} | {self.average()} |'


class Group:

    def __init__(self, group_name):
        self.group_name = group_name
        self.st_list = []
        self.max_stud = 20

    def adds(self, student):
        if not isinstance(student, Student):
            raise Exception('There is no such a student.')
        if len(self.st_list) > self.max_stud:
            raise Exception('There is no more place in the group.')
        if Student.name in self.st_list and Student.surname in self.st_list:
            raise Exception('The student is already assigned.')

        self.st_list.append(student)

    def five_rated(self):
        return sorted(map(Student.average, self.st_list), key=max, reverse=True)[:5]


def main():
    group = Group('MF-20')
    group.adds(Student('Ihor', 'Chornobay', 'MF-20', 1220, [5, 4, 3, 2, 1]))
    group.adds(Student('Ivan', 'Kostomakha', 'MF-20', 1221, [5, 4, 3, 2, 5]))
    group.adds(Student('Maksym', 'Chornovil', 'MF-20', 1223, [5, 5, 5, 5, 1]))
    group.adds(Student('Alina', 'Nechyporenko', 'MF-20', 1224, [5, 5, 2, 5, 4]))
    group.adds(Student('Oleh', 'Nalyvaiko', 'MF-20', 1225, [3, 5, 3, 4, 4]))
    group.adds(Student('Kostyantyn', 'Pyrohov', 'MF-20', 1226, [5, 5, 5, 5, 4]))
    group.adds(Student('Ilona', 'Pakholka', 'MF-20', 1227, [5, 5, 5, 5, 5]))
    five_rated = group.five_rated()
    print(five_rated)


if __name__ == '__main__':
    main()
