from collections import deque

from common import convert_to_node

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recursion(node: TreeNode, max_num: int):
            if not node:
                return 0
            
            if node.val >= max_num:
                return 1 + recursion(node.left, max(max_num, node.val)) + recursion(node.right, max(max_num, node.val))
            else:
                return recursion(node.left, max(max_num, node.val)) + recursion(node.right, max(max_num, node.val))
        
        return recursion(root, root.val)

s = Solution()
# root_list = [3,1,4,3,None,1,5]
# root = convert_to_node(root_list)

# print(s.goodNodes(root))

assert s.goodNodes(convert_to_node([3,1,4,3,None,1,5])) == 4
assert s.goodNodes(convert_to_node([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])) == 5

print("All tests have passed")