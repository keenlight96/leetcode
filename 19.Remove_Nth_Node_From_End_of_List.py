# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert_list_to_linkedlist(arr: List[int]) -> ListNode:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    
    return head

def convert_linkedlist_to_list(node: ListNode) -> List[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = head
        n_node = head
        count = 0
        while curr.next:
            curr = curr.next
            count += 1
            if count > n:
                 n_node = n_node.next
        
        if count == n - 1:
            return head.next
        n_node.next = n_node.next.next
        return head

s = Solution()
arr = [1,2]
head = convert_list_to_linkedlist(arr)
head = s.removeNthFromEnd(head, 2)
print(convert_linkedlist_to_list(head))
        