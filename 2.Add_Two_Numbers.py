from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    mem = 0
    head3 = None
    l3 = None
    while (l1 != None or l2 != None):
        l1 = ListNode(0) if l1 == None else l1
        l2 = ListNode(0) if l2 == None else l2
        res = int(l1.val) + int(l2.val) + mem
        mem = 0
        if res > 9:
            mem = int(res / 10)
            res = res % 10
        
        if l3 == None:
            l3 = ListNode(res)
            head3 = l3
        else:
            l3.next = ListNode(res)
            l3 = l3.next
    
        l1 = l1.next
        l2 = l2.next
    
    if mem != 0:
        l3.next = ListNode(mem)
    
    return head3


arr1 = [9,9,9,9,9,9,9]
l1 = ListNode(arr1[0])
current = l1
for val in arr1[1:]:
    current.next = ListNode(val)
    current = current.next
    
arr2 = [9,9,9,9]
l2 = ListNode(arr2[0])
current2 = l2
for val in arr2[1:]:
    current2.next = ListNode(val)
    current2 = current2.next
    
l3 = addTwoNumbers(l1, l2)
while l3.next != None:
    print(l3.val)

        

            
            