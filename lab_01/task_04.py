import argparse

parser = argparse.ArgumentParser(description='knapsack_game')
parser.add_argument('-W', dest='capacity', type=int)
parser.add_argument('-w', dest='weight', type=list, nargs='+')
args = parser.parse_args()


def datacheck(w, capacity):
    if any(weight <= 0 for weight in w):
        print('Weight of some of the bars must be greater than 0.')
        return False
    if any(weight == weight for weight in w):
        print('Fractions of bar are not allowed.')
        return False
    if capacity <= 0:
        print('It seems your knapsack has a big hole inside. Please, try to set another capacity, '
              '  at least greater than 0.')
        return False
    return True


def knapsack_solution(w, capacity):
    """
    :param list w: weights of items
    :param int capacity: capacity(kg) of knapsack
    """
    n = len(w)
    weight = [0] + w
    table = [[0 for x in range(n)] for y in range(capacity + 1)]

    for i in range(1, n):
        for j in range(1, capacity + 1):
            if weight[i] <= j:
                table[j][i] = max(table[j - weight[i]][i - 1] + weight[i], table[j][i - 1])

    return table[-1][-1]


def main():
    datacheck(args.capacity, args.weight)
    if not datacheck(args.capacity, args.weight):
        return 0
    else:
        print(knapsack_solution(args.capacity, args.weight))


if __name__ == '__main__':
    main()

