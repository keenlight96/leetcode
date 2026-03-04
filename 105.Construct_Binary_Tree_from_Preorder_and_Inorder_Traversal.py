from typing import List, Optional

from common import convert_to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 1
        def find_in_range(list, left, right, target):
            for i in range(left, right):
                if list[i] == target:
                    return i
            return None
        
        root = None
        if len(preorder) > 0:
            root = TreeNode(preorder[0])
        else:
            return root
        
        left = 0
        right = len(preorder)
        in_idx = find_in_range(inorder, left, right, root.val)

        def recursion(node, left, right, isLeft):
            if self.pre_idx < len(preorder):
                in_idx = find_in_range(inorder, left, right, preorder[self.pre_idx])
                if in_idx is not None:
                    new_node = TreeNode(preorder[self.pre_idx])
                    if isLeft:
                        node.left = new_node
                    else:
                        node.right = new_node
                    self.pre_idx += 1
                    recursion(new_node, left, in_idx, True)
                    recursion(new_node, in_idx + 1, right, False)

        recursion(root, left, in_idx, True)
        recursion(root, in_idx + 1, right, False)
        return root

s = Solution()
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]

# root = s.buildTree(preorder, inorder)
# print(convert_to_list(root))

assert convert_to_list(s.buildTree([3,9,20,15,7], [9,3,15,20,7])) == [3,9,20,None,None,15,7]
assert convert_to_list(s.buildTree([-1], [-1])) == [-1]

print("All tests have passed")