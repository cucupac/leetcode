# Definition for a binary tree node.
# TODO: do this problem again.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    # Recur on left child and right child
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Calculate the depth of the current node
    node_depth = max(left_depth, right_depth) + 1

    return node_depth


# Driver code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Preorder traversal of binary tree is")
print(maxDepth(root))
