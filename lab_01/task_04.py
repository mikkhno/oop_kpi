import argparse

parser = argparse.ArgumentParser(description='knapsack_game')
parser.add_argument('-W', '--capacity', type=int)
parser.add_argument('-w', '--weight', type=list, nargs='+')
parser.add_argument('-n', '--amount', type=int)
args = parser.parse_args()


def knapsack(n, w, c):
    """
    :param int n: number of items
    :param list w: weights of items
    :param int c: capacity of knapsack
    """
    # list_e = [[0 for x in range(n)] for y in range(c)]
    #
    # for i in range(1, n + 1):
    #     for a in range(1, c + 1):
    #         if w[i] > a:
    #             list_e[i][a] = list_e[i - 1][a]
    #         else:
    #             if (w[i] + list_e[i - 1][c - w[i]]) > list_e[i - 1][a]:
    #                 list_e[i][a] = w[i] + list_e[i - 1][a - w[i]]
    #             else:
    #                 list_e[i][a] = list_e[i - 1][a]

    # return list_e[n][a]

    max_weight = [[w[x] for x in range(n)] for y in range(c)]

    for i in range(1, n + 1):
        for k in range(1, c + 1):
            if max_weight[i][k] > c:
                max_weight[i][k] = max_weight[i - 1][k]
            else:
                if (max_weight[i][k] + max_weight[i - 1][c - max_weight[i][k]]) > max_weight[i - 1][k]:
                    max_weight[i][k] = max_weight[i][k] + max_weight[i - 1][c - max_weight[i][k]]
                else:
                    max_weight[i][k] = max_weight[i - 1][k]

    return max_weight[i][k]


if __name__ == '__main__':
    w = [5, 3, 1, 7]
    print(knapsack(4, w, 10))
