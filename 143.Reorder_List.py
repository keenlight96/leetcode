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
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        if not head:
            return None
        
        curr = head
        prev = None
        nextNode = None
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        # find middle element
        slow = head
        fast = head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the right part
        right_head = self.reverse(slow.next)
        
        # merge 2 parts
        curr = head
        while curr != slow:
            next_node = curr.next
            right_node = right_head.next
            curr.next = right_head
            curr.next.next = next_node
            right_head = right_node
            curr = next_node
        
        if curr == curr.next.next:
            curr.next = None


# data
s = Solution()
arr = [1,2,3,4,5]
head = convert_list_to_linkedlist(arr)
# reversed_head = s.reverse(head)
# print(convert_linkedlist_to_list(reversed_head))
s.reorderList(head)
print(convert_linkedlist_to_list(head))
        