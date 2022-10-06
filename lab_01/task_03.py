import argparse

parser = argparse.ArgumentParser(description='ebnf')
parser.add_argument('f_string', type=str)
args = parser.parse_args()


# bool function for validating
def checking():
    # adding recognisable signs as operators
    signs = ('+', '-')
    previous_symbol = ''
    # adding bool for validating the string
    is_valid = True

    # checking if symbol is numeric or sign, order and if it is not the end of string
    if args.f_string:
        for symbol in args.f_string:
            if symbol.isnumeric() or (symbol in signs and previous_symbol.isnumeric() and symbol != args.f_string[-1]):
                previous_symbol = symbol
            else:
                is_valid = False
                break
    else:
        is_valid = False

    return is_valid


def main():
    print(checking())
    if checking():
        print(eval(args.f_string))
    else:
        print('None')


if __name__ == '__main__':
    main()
