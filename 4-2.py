# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

# Example [ 11, 13, 14, 15, 16, 17, 18, 20, 23, 30, 33, 40, 42, 43]
#
# As a tree:
#
#                    20
#           15                40
#       13      17        30      43
#     11  14  16  18    23  33  42
#
#
# Some notes:
# The root node will always be round(len(list) / 2)
# The number of layers will always be ceil(log2(len(list)))

############################### Handy code for printing the tree ################################
# From: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python #
#################################################################################################

def display(tree):
    lines, _, _, _ = _display_aux(tree)
    for line in lines:
        print(line)

def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right is None and node.left is None:
        line = '%s' % node.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = '%s' % node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = '%s' % node.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

###############################################################################################################

class node:
    def __init__(self, val, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right

def createTree(myList):
    # Only two items left, node and left child
    if len(myList) < 3:
        return node(myList[1], node(myList[0]))

    # Three items, node with left and right child
    elif len(myList) == 3:
        return node(myList[1], node(myList[0]), node(myList[2]))

    # More than three items, keep breaking it down
    else:
        mid = int(len(myList) / 2)
        return node(myList[mid], createTree(myList[:mid]), createTree(myList[mid+1:]))

list1 = [ 11, 13, 14, 15, 16, 17, 18, 20, 23, 30, 33, 40, 42, 43]
top = createTree(list1)
display(top)

######### Example output ##########
#                                 #
#         ______20_______         #
#        /               \        #
#     __15___         __40___     #
#    /       \       /       \    #
#   13_     17_     30_     43    #
#  /   \   /   \   /   \   /      #
# 11  14  16  18  23  33  42      #
