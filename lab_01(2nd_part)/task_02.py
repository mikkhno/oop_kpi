import math


class Rational:
    """
    :param int numerator: numerator of the performing fraction
    :param int denominator: denominator of the performing fraction

    """

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, num_value):
        if not isinstance(num_value, int):
            raise TypeError()
        self.__numerator = num_value

    @numerator.getter
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, den_value):
        if not isinstance(den_value, int):
            raise TypeError()
        if den_value == 0:
            raise ZeroDivisionError()
        self.__denominator = den_value

    @denominator.getter
    def denominator(self):
        return self.__denominator

    # function that helps to get the fraction simplified
    def simplifier(self):
        common = math.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    # function that shows simplified fraction
    def show_fraction(self):
        self.simplifier()
        return f'entered fraction is {self.numerator} / {self.denominator}'

    # function that returns performed fraction as a string
    def show_result(self):
        return str(self.numerator / self.denominator)

    def __str__(self):
        return f'{self.show_fraction()} and performed is {self.show_result()}'


def main():
    num = int(input('enter the numerator:'))
    den = int(input('enter the denominator:'))
    frac = Rational(num, den)
    print(frac)


if __name__ == '__main__':
    main()