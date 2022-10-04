import argparse

parser = argparse.ArgumentParser(description='ebnf')
parser.add_argument('f_string', type=str)
args = parser.parse_args()


def checking():

    signs = ('+', '-')
    previous_symbol = ''
    is_valid = True

    if args.f_string:
        for symbol in args.f_string:
            if symbol.isnumeric() or (symbol in signs and previous_symbol.isnumeric() and symbol !=args.f_string[-1]):
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