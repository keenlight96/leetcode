# Definition for a Node.
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nHead = Node(head.val)
        nCurr = nHead
        curr = head.next
        dict1 = defaultdict()
        dict2 = defaultdict()
        count = 0
        dict1[head] = count
        dict2[count] = nHead
        
        while curr:
            nCurr.next = Node(curr.val)
            nCurr = nCurr.next
            
            count += 1
            dict1[curr] = count
            dict2[count] = nCurr
            
            curr = curr.next
        
        curr = head
        nCurr = nHead
        while curr:
            if curr.random:
                idx = dict1[curr.random]
                nCurr.random = dict2[idx]
            else:
                nCurr.random = None
            
            curr = curr.next
            nCurr = nCurr.next
        
        return nHead

s = Solution()

h4 = Node(1, None, None)
h3 = Node(10, h4, None)
h2 = Node(11, h3, None)
h1 = Node(13, h2, None)
h0 = Node(7, h1, None)

h0.random = None
h1.random = h0
h2.random = h4
h3.random = h2
h4.random = h0
res = s.copyRandomList(h0)