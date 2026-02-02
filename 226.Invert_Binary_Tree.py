from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Special case
        if not root or (root.left == None and root.right == None):
            return root
        
        # Normal case
        node = root
        self.invertTreeHelper(node)
        
        return root
    
    def invertTreeHelper(self, node: TreeNode):
        if not node or (node.left == None and node.right == None):
            return node
        
        node.left, node.right = node.right, node.left
        self.invertTreeHelper(node.left)
        self.invertTreeHelper(node.right)


# root_arr = [4,2,7,1,3,6,9]
# node1 = TreeNode(1)
# node2 = TreeNode(3)
# node3 = TreeNode(6)
# node4 = TreeNode(9)
# node5 = TreeNode(2, node1, node2)
# node6 = TreeNode(7, node3, node4)
# node7 = TreeNode(4, node5, node6)
# root = node7

node1 = TreeNode(None)
node2 = TreeNode(2)
node3 = TreeNode(1, None, node2)
root = node3

solution = Solution()
s = solution.invertTree(root)
print()