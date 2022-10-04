import argparse

parser = argparse.ArgumentParser(description='knapsack_game')
parser.add_argument('-W', '--capacity', type=int)
parser.add_argument('-w', '--weight',  type=int, nargs='+')
parser.add_argument('-n', '--amount',  type=int)
args = parser.parse_args()

n = args.amount
c = args.capacity


def table_of_performing(n, c):

    table = [n][c]
    #w - maximal weight
    w = [n]
    result = None

    if table[n][c]:
        return table[n][c]

    if not n or not c:
        result = 0
    else:
        if w[n] > c:
            result = table_of_performing(n-1, c)

        else:
            tmp1 = table_of_performing(n-1, c)
            tmp2 = table_of_performing(n-1, c - w[n])
            result = max(tmp1, tmp2)

        result = table[n][c]
        return result

    if __name__ == '__main__':
        print(table_of_performing(n, c))












