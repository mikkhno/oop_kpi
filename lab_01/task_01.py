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


def main():
    if args.operation == '/' and (args.num1 == 0 or args.num2 == 0):
        print('Dividing by zero.')
        return 0

    math_operation(args.num1, args.operation, args.num2)

    if not math_operation(args.num1, args.operation, args.num2):
        print('Missing operation.')
        return 0
    else:
        print(math_operation(args.num1, args.operation, args.num2))


if __name__ == '__main__':
        main()

