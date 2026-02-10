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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: TreeNode, q: TreeNode):
            if p is None and q is None:
                return True
            elif (p is not None and q is None) or (p is None and q is not None) or (p.val != q.val):
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def recursion(node: TreeNode):
            if node is None:
                return False
            
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            else:
                return recursion(node.left) or recursion(node.right)
        
        return recursion(root)

s = Solution()
root_list = [3,4,5,1,2]
subRoot_list = [4,1,2]
root = convertToNode(root_list)
subRoot = convertToNode(subRoot_list)

# print(s.isSubtree(root, subRoot))

assert s.isSubtree(convertToNode([3,4,5,1,2]), convertToNode([4,1,2])) == True
assert s.isSubtree(convertToNode([3,4,5,1,2,None,None,None,None,0]), convertToNode([4,1,2])) == False

print("All tests passed")