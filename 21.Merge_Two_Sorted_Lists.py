# Definition for singly-linked list.
from typing import List, Optional

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

def convert_linkedlist_to_list(node: ListNode) -> List[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 and not list2:
            head = ListNode(list1.val)
            list1 = list1.next
        elif list2 and not list1:
            head = ListNode(list2.val)
            list2 = list2.next
        elif list1 and list2:
            if list1.val < list2.val:
                head = ListNode(list1.val)
                list1 = list1.next
            else:
                head = ListNode(list2.val)
                list2 = list2.next
        
        node = head
        while list1 or list2:
            if not list1 or (list2 and list1.val >= list2.val):
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
            elif not list2 or (list1 and list1.val <= list2.val):
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
        
        return head

s = Solution()
list1 = convert_list_to_linkedlist([])
list2 = convert_list_to_linkedlist([0])
head = s.mergeTwoLists(list1, list2)
print(convert_linkedlist_to_list(head))