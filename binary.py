r"""
Assessment 3.3 - Non-Linear Data Structure
Program 1: Binary Tree using the last name FUENTES  (BFS and DFS traversal)

The letters of FUENTES are placed level by level. The two E's are different
nodes that carry the same letter.

              F              level 0
           /     \
         U         E         level 1
        / \       / \
       N   T     E   S       level 2
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """Build the binary tree from the diagram."""
    root = Node("F")
    root.left, root.right = Node("U"), Node("E")
    root.left.left, root.left.right = Node("N"), Node("T")
    root.right.left, root.right.right = Node("E"), Node("S")
    return root


def bfs(root):
    """Breadth-First Search: visit level by level, left to right (uses a queue)."""
    order = []
    if root is None:
        return order
    queue = deque([root])
    while queue:
        node = queue.popleft()          # take from the front
        order.append(node.value)        # visit
        if node.left:
            queue.append(node.left)     # add children to the back
        if node.right:
            queue.append(node.right)
    return order


def dfs(node, order=None):
    """Depth-First Search (pre-order): go as deep as possible before backtracking."""
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.value)            # visit
    dfs(node.left, order)               # go deep into the left subtree
    dfs(node.right, order)              # then the right subtree
    return order


if __name__ == "__main__":
    root = build_tree()
    print("BFS:", " - ".join(bfs(root)))
    print("DFS:", " - ".join(dfs(root)))