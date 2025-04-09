import sys

N = int(sys.stdin.readline())
tree = {}


class Node:

    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    if node.item != '.':
        print(node.item, end='')

    if node.left != '.':
        preorder(tree[node.left])
        
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):

    if node.left != '.':
        inorder(tree[node.left])

    if node.item != '.':
        print(node.item, end='')

    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):

    if node.left != '.':
        postorder(tree[node.left])

    if node.right != '.':
        postorder(tree[node.right])

    if node.item != '.':
        print(node.item, end='')


for i in range(N):
    item, left, right = map(str, sys.stdin.readline().split())
    tree[item] = Node(item, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

print(tree)