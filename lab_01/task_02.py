import argparse
import math
import operator


def math():
    parser = argparse.ArgumentParser(description="Calculating universal math operations")
    parser.add_argument('operators', type=str)
    parser.add_argument('num1', type=float)
    parser.add_argument('num2', type=float)
    args = parser.parse_args()

    # we are checking if there is no dividing by zero
    if (args.operators == 'truediv' or args.operators == 'floordiv') and (args.num1 == 0 or args.num2 == 0):
        print('Dividing by zero.')
        return 0

    performing = getattr(math, args.operators, None)

    # we are checking library compatibility
    if not performing:
        performing = getattr(operator, args.operators, None)

    # if we have unrecognised operation, this condition will inform us, otherwise showing the results
    if not performing:
        print('Math operation has not been detected.')
        return None

    print(performing(args.num1, args.num2))


if __name__ == '__main__':
    math()

