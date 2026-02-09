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


# solution = Solution()

# node1 = TreeNode(3)
# node2 = TreeNode(2)
# node3 = TreeNode(1, node1, node2)
# print(solution.maxDepth(node3))


# Tree Node helpers
def convertToNode(arr: list) -> TreeNode:
    # count = len(arr)
    # level = 0
    # while count > 0:
    #     count -= 2**level
    #     level += 1
    if len(arr) == 0:
        return None

    d = deque(arr)
    root = TreeNode(d.popleft())
    node = root
    nodes = deque([])

    while len(d) > 0:
        if len(nodes) > 0:
            node = nodes.popleft()

        node_left = TreeNode(d.popleft())
        node_right = TreeNode(None)
        if len(d) > 0:
            node_right = TreeNode(d.popleft())
        nodes.extend([node_left, node_right])
        node.left = node_left if node_left.val is not None else None
        node.right = node_right if node_right.val is not None else None

    return root


def convertToList(root: TreeNode) -> list:
    node_list = []
    level = 0
    count = 0
    have_available_nodes = False
    nodes = deque([root])
    while len(nodes) > 0:
        node = nodes.popleft()
        count += 1
        if count > 2**level:
            if not have_available_nodes:
                break
            count = 0
            have_available_nodes = False

        if node is not None:
            have_available_nodes = True
            node_list.append(node.val)
            nodes.extend([node.left, node.right])
        else:
            node_list.append(None)
            nodes.extend([None, None])

    # remove last None(s)
    while node_list[-1] is None:
        node_list.pop()
    return node_list


node_list = [3, 9, 20, None, None, 15, 7]
root = convertToNode(node_list)
print()

node_list_2 = convertToList(root)
print(node_list_2)
        
