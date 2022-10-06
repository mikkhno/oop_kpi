import argparse

parser = argparse.ArgumentParser(description='ebnf')
parser.add_argument('f_string', type=str)
args = parser.parse_args()


# bool function for validating the expression
def checking():
    # adding recognisable signs as the simple math operations
    signs = ('+', '-')
    previous_symbol = ''

    # checking if symbol is numeric or sign, order and if it is not the end of string
    if args.f_string:
        for symbol in args.f_string:
            if symbol.isnumeric() or (symbol in signs and previous_symbol.isnumeric() and symbol != args.f_string[-1]):
                previous_symbol = symbol
            else:
                return False
    else:
        return False

    return True


def main():
    print(checking())
    if checking():
        print(eval(args.f_string))
    else:
        print('None')


if __name__ == '__main__':
    main()
