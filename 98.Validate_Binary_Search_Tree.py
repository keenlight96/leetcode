from typing import Optional

from common import convert_to_node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(node: TreeNode, min_val: int, max_val: int):
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            return recursion(node.left, min_val, node.val) and recursion(node.right, node.val, max_val)
        
        return recursion(root, float("-inf"), float("inf"))

s = Solution()
# root_list = [5,4,6,None,None,3,7]
# root = convert_to_node(root_list)

# print(s.isValidBST(root))

assert s.isValidBST(convert_to_node([2,1,3])) == True
assert s.isValidBST(convert_to_node([5,1,4,None,None,3,6])) == False
assert s.isValidBST(convert_to_node([5,4,6,None,None,3,7])) == False

print("All tests have passed!")