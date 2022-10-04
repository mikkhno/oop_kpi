import argparse
import math
import operator


def math():
    parser = argparse.ArgumentParser(description="Calculating universal math operations")
    parser.add_argument('operators', type=str)
    parser.add_argument('num1', type=float)
    parser.add_argument('num2', type=float)
    args = parser.parse_args()

    performing = getattr(math, args.operators, None)

    if not performing:
        performing = getattr(operator, args.operators, None)

    if not performing:
        print('Math operation has not been detected.')
        return None

    print(performing(args.num1, args.num2))


if __name__ == '__main__':
    math()

