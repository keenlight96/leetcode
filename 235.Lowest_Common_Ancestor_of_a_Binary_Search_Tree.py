from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


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

class Solution:
    def lowestCommonAncestor_bak(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ancestor = None
        def recursion(node: TreeNode):
            if self.ancestor != None:
                return True
            
            if not node:
                return False
            
            left = recursion(node.left)
            right = recursion(node.right)
            
            if left and right:
                self.ancestor = node if not self.ancestor else self.ancestor
                return True
            
            if left or right:
                if node.val == p.val or node.val == q.val:
                    self.ancestor = node if not self.ancestor else self.ancestor
                return True
            
            if node.val == p.val or node.val == q.val:
                return True
            
            return False
        
        recursion(root)
        return self.ancestor
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(node: TreeNode):
            if node.val > p.val and node.val > q.val:
                return recursion(node.left)
            elif node.val < p.val and node.val < q.val:
                return recursion(node.right)
            return node
        
        return recursion(root)

s = Solution()
# root_list = [6,2,8,0,4,7,9,None,None,3,5]
# root = convertToNode(root_list)
# p = TreeNode(2)
# q = TreeNode(8)

# print(s.lowestCommonAncestor(root, p, q).val)

assert s.lowestCommonAncestor(convertToNode([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(8)).val == 6
assert s.lowestCommonAncestor(convertToNode([6,2,8,0,4,7,9,None,None,3,5]), TreeNode(2), TreeNode(4)).val == 2
assert s.lowestCommonAncestor(convertToNode([2,1]), TreeNode(2), TreeNode(1)).val == 2
assert s.lowestCommonAncestor(convertToNode([3,1,4,None,2]), TreeNode(2), TreeNode(3)).val == 3

print("All tests passed")