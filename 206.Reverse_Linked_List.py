from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        rev = ListNode(val=head.val, next=None)
        
        while head.next:
            head = head.next
            rev = ListNode(val=head.val, next=rev)
        
        return rev

s = Solution()
arr = [1,2,3,4,5]
head = convert_list_to_linkedlist(arr)

print(s.reverseList(head).val)