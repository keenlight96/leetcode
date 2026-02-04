from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     return self.diameterOfBinaryTreeHelper(root, 0, 0)[1]

    # def diameterOfBinaryTreeHelper(self, node: Optional[TreeNode], depth: int, max_diameter: int) -> tuple:
    #     if not node:
    #         return 0, 0

    #     depth_left, max_diameter_left = self.diameterOfBinaryTreeHelper(node.left, depth + 1, max_diameter)
    #     depth_right, max_diameter_right = self.diameterOfBinaryTreeHelper(node.right, depth + 1, max_diameter)

    #     return max(depth_left, depth_right) + 1, max(max_diameter, max_diameter_left, max_diameter_right, depth_left + depth_right)

    ### Best way
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def helper(node):
            if not node:
                return 0

            depth_left = helper(node.left)
            depth_right = helper(node.right)
            
            self.diameter = max(self.diameter, depth_left + depth_right)

            return max(depth_left, depth_right) + 1

        helper(root)
        return self.diameter


solution = Solution()
node_list = [0, 1, 2, 3, 4]
root = convertToNode(node_list)

print(solution.diameterOfBinaryTree(root))
