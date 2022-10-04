import argparse

parser = argparse.ArgumentParser(description='Calculating simple math operations')
parser.add_argument('num1', type=float)
parser.add_argument('operation', type=str)
parser.add_argument('num2', type=float)
args = parser.parse_args()


def math_operation(num1, operation, num2):

    if operation == '+':
        return num1 + num2

    if operation == '-':
        return num1 - num2

    if operation == '*':
        return num1 * num2

    if operation == '/':
        return num1 / num2

    else:
        return None


if __name__ == '__main__':
        print(math_operation(args.num1, args.operation, args.num2))

