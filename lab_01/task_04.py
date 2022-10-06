import argparse

parser = argparse.ArgumentParser(description='knapsack_game')
parser.add_argument('-W', dest='capacity', type=int)
parser.add_argument('-w', dest='weight', type=list, nargs='+')
args = parser.parse_args()


# checking if everything is ok with data from shell
def datacheck():
    if any(weight <= 0 for weight in args.weight):
        print('Weight of some of the bars must be greater than 0.')
        return False
    if any((args.weight == args.weight) for weight in args.weight):
        print('Fractions of bar are not allowed.')
        return False
    if args.capacity <= 0:
        print('It seems your knapsack has a big hole inside. Please, try to set another capacity, '
              '  at least greater than 0.')
        return False
    return True


# knapsack problem solution
def knapsack_solution(w, capacity):
    """
    :param list w: weights of items
    :param int capacity: capacity(kg) of knapsack
    """
    n = len(w)
    weight = [0] + w
    # setting the helping array 'table' for finding the most optimal option
    table = [[0 for x in range(n)] for y in range(capacity + 1)]

    # comparing the max value for all values in array
    for i in range(1, n):
        for j in range(1, capacity + 1):
            if weight[i] <= j:
                table[j][i] = max(table[j - weight[i]][i - 1] + weight[i], table[j][i - 1])
    # returning the result
    return table[-1][-1]


def main():
    datacheck()
    if not datacheck():
        return 0
    else:
        print(knapsack_solution(args.weight, args.capacity))


if __name__ == '__main__':
    main()
