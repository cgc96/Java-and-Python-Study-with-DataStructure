class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node, left_node ,right_node):
        if self.root == None:
            self.root = node

        node.left = left_node
        node.right = right_node

    def inorder(self, node):
        if not node.left == None:
            self.inorder(node.left)

        print(node.data, end='')

        if not node.right == None:
            self.inorder(node.right)

    def preorder(self, node):
        print(node.data, end='')

        if not node.left == None:
            self.preorder(node.left)

        if not node.right == None:
            self.preorder(node.right)


    def postorder(self, node):
        if not node.left == None:
            self.postorder(node.left)

        if not node.right == None:
            self.postorder(node.right)

        print(node.data, end='')


if __name__ == "__main__":
    n = int(input())

    t = Tree()
    node = []
    for i in range(26):
        node.append(Node(chr(i+65)))


    for i in range(n):
        temp = input()
        point = node[ord(temp[0])-65]
        point_left = None
        point_right = None

        if not temp[2] == '.':
            point_left = node[ord(temp[2])-65]

        if not temp[4] == '.':
            point_right = node[ord(temp[4])-65]

        t.insert(point, point_left, point_right)

    t.preorder(t.root)
    print()
    t.inorder(t.root)
    print()
    t.postorder(t.root)

