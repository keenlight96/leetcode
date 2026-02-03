from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Special case
        if not root:
            return 0

        # Normal case
        return self.maxDepthHelper(root, 0, 0)

    def maxDepthHelper(self, node: TreeNode, depth: int, maxDepth: int) -> int:
        if not node:
            return maxDepth

        depth += 1
        if depth > maxDepth:
            maxDepth = depth

        maxDepth = self.maxDepthHelper(node.left, depth, maxDepth)
        maxDepth = self.maxDepthHelper(node.right, depth, maxDepth)

        return maxDepth

### Best solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)

        return 1 + max(depthLeft, depthRight)


solution = Solution()

node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(1, node1, node2)
print(solution.maxDepth(node3))


# def convertToNode(arr: list):
#     # count = len(arr)
#     # level = 0
#     # while count > 0:
#     #     count -= 2**level
#     #     level += 1
#     if len(arr) == 0:
#         return None
    
#     d = deque(arr)
#     root = TreeNode(d.popleft())
#     node = root
#     nodes = []
    
#     while len(d) > 0:
#         node_left = TreeNode(d.popleft())
#         node_right = TreeNode(d.popleft())
#         nodes.
#         node.left = node_left
#         node.right = node_right


# root = [3, 9, 20, None, None, 15, 7]
# print(convertToNode(root))
