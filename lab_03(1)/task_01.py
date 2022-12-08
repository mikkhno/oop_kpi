from fractions import Fraction

operations = ["+", "-", "/", "*", "?"]


class Operation:
    def __init__(self, num1=1, den1=1, sign='', num2=1, den2=1):
        self.num1 = num1
        self.num2 = num2
        self.den1 = den1
        self.den2 = den2
        self.sign = sign

        @property
        def den1(self):
            return self.__den1

        @den1.setter
        def den1(self, n):
            if n == 0:
                raise ZeroDivisionError()
            self.__den1 = n

        @den1.getter
        def den1(self):
            return self.__den1

        @property
        def den2(self):
            return self.__den2

        @den2.setter
        def den2(self, n):
            if n == 0:
                raise ZeroDivisionError()
            self.__den2 = n

        @den2.getter
        def den1(self):
            return self.__den2

    def operation(self):
        if self.sign == "+":
            return (Fraction(self.num1, self.den1) + Fraction(self.num2, self.den2))

        if self.sign == "-":
            return (self.num1, self.den1 - Fraction(self.num2, self.den2))

        if self.sign == "/":
            return (Fraction(self.num1,self.den1) / Fraction(self.num2,self.den2))

        if self.sign == "*":
            return (Fraction(self.num1, self.den1) * Fraction(self.num2, self.den2))

        if self.sign == "?":
            return max(Fraction(self.num1, self.den1),
                  Fraction(self.num2,self.den2))

        raise TypeError("Operation is not found.")

    def __str__(self):

        return f'result: {self.operation()}'



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