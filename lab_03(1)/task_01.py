import math
from fractions import Fraction

#   final overview(1):
#   1/4 + 5/4 [Enter]
#   |result:3/2 or 1.5

operations = ["+", "-", "/", "*", "?"]


class Operation:
    def __init__(self, num1=1, den1=1, sign='', num2=1, den2=1):
        self.num1 = num1
        self.num2 = num2
        self.den1 = den1
        self.den2 = den2
        self.sign = sign
        self.result = 0

        @property
        def sign(self):
            return self.__sign

        @sign.setter
        def sign(self, op):
            if not isinstance(op, str):
                raise TypeError()
            if not op in operations:
                raise TypeError("Operation is not found.")
            self.__sign = op

        @sign.getter
        def den2(self):
            return self.__den2

    def operation(self):
        if self.sign == "+":
            self.result = (Fraction(self.num1, self.den1) + Fraction(self.num2, self.den2))

        if self.sign == "-":
            self.result = (self.num1, self.den1 - Fraction(self.num2, self.den2))

        if self.sign == "/":
            self.result = (Fraction(self.num1,self.den1) / Fraction(self.num2,self.den2))

        if self.sign == "*":
            self.result = (Fraction(self.num1, self.den1) * Fraction(self.num2, self.den2))

        if self.sign == "?":
            self.result = max(Fraction(self.num1, self.den1),
                  Fraction(self.num2,self.den2))

    def __str__(self):
        self.operation()
        return f'result: {self.result}'


def main():
    expr = input("enter the expression: ").split(sep=' ')
    sign = expr[1]
    rational1 = expr[0].split(sep="/")
    rational2 = expr[2].split(sep="/")
    print(expr, rational1, rational2)
    operation = Operation(int(rational1[0]), int(rational1[1]), sign, int(rational2[0]),int(rational2[1]))
    print(operation)


if __name__ == "__main__":
    main()