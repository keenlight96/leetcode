from typing import List, Optional

# Definition for singly-linked list.
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
    def mergeKLists_bak(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                lists.pop(i)
        if not lists:
            return None
        
        head = None
        curr = head
        while lists:
            lists.sort(key=lambda x: x.val)
            if not head:
                head = ListNode(lists[0].val)
                curr = head
            else:
                curr.next = ListNode(lists[0].val)
                curr = curr.next
            
            if lists[0].next:
                lists[0] = lists[0].next
            else:
                lists.pop(0)

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide_and_conquer(lists, 0, len(lists)-1)
    
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list2.next, list1)
            return list2
    
    def divide_and_conquer(self, lists: List[Optional[ListNode]], left: int, right: int):
        if left == right:
            return lists[left]
        
        mid = left + (right - left) // 2
        list1 = self.divide_and_conquer(lists, left, mid)
        list2 = self.divide_and_conquer(lists, mid + 1, right)
        return self.merge(list1, list2)

arrs = [[1,4,5],[1,3,4],[2,6]]
lists = []
for arr in arrs:
    head = convert_list_to_linkedlist(arr)
    lists.append(head)

s = Solution()
print(convert_linkedlist_to_list(s.mergeKLists(lists)))
