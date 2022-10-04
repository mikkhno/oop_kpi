import argparse

parser = argparse.ArgumentParser(description='ebnf')
parser.add_argument('f_string', type=str)
args = parser.parse_args()

#create main() and operate() function to return False/None if the code doesn't fit EBNF requirements, and in the
#opposite case - True/Value


def operate():

    signs = ['+', '-']
    previous_symbol = ''
    is_valid = True

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
    result = operate()
    if result:
        print(result, eval(args.f_string))
    else:
        print(result, None)


if __name__ == '__main__':
    main()