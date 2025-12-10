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
    def reversePartition(self, head: Optional[ListNode], k: int) -> Optional[tuple[ListNode, ListNode]]:
        # reverse first k nodes and return (head, tail) and the original k-th node
        # if not enough k nodes, return None
        
        if head is None:
            return None
        tail = ListNode(head.val, None)
        rev = tail
        for i in range(1, k):
            if head.next:
                head = head.next
                rev = ListNode(head.val, rev)
            else:
                return None
        return (rev, tail, head)
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # case 1 node
        if not head.next:
            return head
        
        # case normal
        # with constrain, there is no case that reversePartition return None in the first call
        first_head = None
        prev_tail = None
        while head:
            partition = self.reversePartition(head, k)
            # if enough k nodes left to reverse
            if partition:
                (rev_head, rev_tail, head) = partition
                head = head.next
                
                # ressign head of result linkedlist
                if not first_head:
                    first_head = rev_head
                
                # join previous tail with new reversed head
                if prev_tail:
                    prev_tail.next = rev_head
                    
                # save the tail
                prev_tail = rev_tail
            else:
                # join previous tail with the first of left nodes
                if prev_tail:
                    prev_tail.next = head
                break
        return first_head

arr = [1,2,3,4,5]
head = convert_list_to_linkedlist(arr)

s = Solution()
res = s.reverseKGroup(head, 4)
print(convert_linkedlist_to_list(res))