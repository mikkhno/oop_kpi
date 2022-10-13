class Node:
    def __init__(self, key, price):
        self.left = None
        self.right = None
        self.key = key
        self.price = price
        self.qty = 0
        self.tree = []

    # inserting node
    def insert(self, key, price):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key, price)
                else:
                    self.left.insert(key, price)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, price)
                else:
                    self.right.insert(key, price)
            if price < 0:
                raise Exception('The price cannot be less than 0')
            if price == 0:
                raise Exception('The price cannot be 0.')
        else:
            self.key = key
            self.price = price

    # printing the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.key),
        if self.right:
            self.right.PrintTree()

    # inorder traversal
    def inordertr(self, root):
        self.tree = []
        if root:
            self.tree = self.inordertr(root.left)
            self.tree.append(root.key)
            self.tree = self.tree + self.inordertr(root.right)
        return self.tree

    def searching(self, node, solve):
        if node.key == solve:
            return node.price

        if not node:
            raise Exception('There is no such a node.')

        left = self.searching(node.left, solve)

        if left:
            return left

        right = self.searching(node.right, solve)
        return right

    def calculating(self, node, solve, qty):
        return qty * self.searching(node, solve)


def main():
    root = Node(1, 20)
    root.insert(2, 30)
    root.insert(4, 10)
    root.insert(7, 15)
    root.insert(6, 100)
    root.insert(3, 12)
    root.insert(5, 42)
    root.inordertr(root)
    key = int(input('enter the code:'))
    quantity = int(input('enter the quantity:'))
    print(root.calculating(root, key, quantity))


if __name__ == '__main__':
    main()