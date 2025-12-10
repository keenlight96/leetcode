# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def convert_list_to_linkedlist(arr: List[int]) -> ListNode:
    head = None
    
    for num in arr:
        if not head:
            head = ListNode(num)
            prev = head
        else:
            new = ListNode(num)
            prev.next = new
            prev = new
    return head

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        set1 = set()
        while head:
            count += 1
            set1.add(head)
            if len(set1) < count:
                return True
            head = head.next

        return False
    
    # two pointers
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        
        while fast:
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        
        return False


s = Solution()
h1 = ListNode(3)
h2 = ListNode(2)
h1.next = h2
h3 = ListNode(0)
h2.next = h3
h4 = ListNode(-4)
h3.next = h4
h4.next = h2
print(s.hasCycle2(h1))