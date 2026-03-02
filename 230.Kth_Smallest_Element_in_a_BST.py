from typing import Optional

from common import convert_to_node


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0
        
        def recursion(node: TreeNode):
            if not node:
                return
            
            recursion(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
            recursion(node.right)
        
        recursion(root)
        return self.res

s = Solution()
# print(s.kthSmallest(convert_to_node([3,1,4,None,2]), 1))

assert s.kthSmallest(convert_to_node([3,1,4,None,2]), 1) == 1
assert s.kthSmallest(convert_to_node([5,3,6,2,4,None,None,1]), 3) == 3
print("All tests have passed")
            
            
            