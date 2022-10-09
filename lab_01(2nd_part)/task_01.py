class Rectangle:
    """
    :param float width: width of Rectangle
    :param float height: height of Rectangle
    """

    def __init__(self, width=1.0, length=1.0):
        self.length = length
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        if not isinstance(w_value, int | float):
            raise TypeError()
        if w_value <= 0 or w_value >= 20:
            raise TypeError()

        self.__width = w_value

    @width.getter
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, l_value):
        if not isinstance(l_value, int | float):
            raise TypeError()

        if l_value <= 0 or l_value >= 20:
            raise TypeError()

        self.__length = l_value

    @length.getter
    def length(self):
        return self.__length

    # performing perimeter of Rectangle
    def perimeter(self):
        return 2 * (self.width + self.length)

    # performing square of Rectangle
    def square(self):
        return self.width * self.length

    def __str__(self):
        return f'width - {self.width} length - {self.length}'


def main():
    rec = Rectangle(4.7, 7)
    print(rec)
    print('Perimeter is', rec.perimeter(), sep=':')
    print('Square is', rec.square(), sep=':')

    rec1 = Rectangle(5, 20)
    rec2 = Rectangle('hi', 9)


if __name__ == '__main__':
    main()
