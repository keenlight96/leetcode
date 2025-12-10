# class LRUCache:

#     def __init__(self, capacity: int):
#         self.store = dict()
#         self.capacity = capacity
#         self.head_key = None
#         self.last = None
        
#     def get(self, key: int) -> int:
#         if key in self.store.keys():
#             self.last = self.store[key]
            
#             if self.store[key].prev:
#                 self.store[key].prev.next = self.store[key].next
#             if self.store[key].next:
#                 self.store[key].next.prev = self.store[key].prev
#             if key == self.head_key:
#                 self.head_key = self.store[key].key
#             return self.store[key].value
        
#     def put(self, key: int, value: int) -> None:
#         if key not in self.store.keys():
#             self.store[key] = Node(key, value, self.last)
#             if self.last:
#                 self.last.next = self.store[key]
#             self.last = self.store[key]
#             if not self.head_key:
#                 self.head_key = key
#             elif len(self.store) > self.capacity:
#                 self.store[self.head_key] = self.store[self.head_key].next
#                 self.store[self.head_key].next.prev = None
#                 self.store.pop(self.head_key)
#         else:
#             self.store[key].value = value
#             self.last = self.store[key]
            
#             if self.store[key].prev:
#                 self.store[key].prev.next = self.store[key].next
#             if self.store[key].next:
#                 self.store[key].next.prev = self.store[key].prev
#             if key == self.head_key:
#                 self.head_key = self.store[key].key
        
        
        
# class Node:
#     def __init__(self, key: int, value: int, prev=None, next=None):
#         self.key = key
#         self.value = value
#         self.prev = prev
#         self.next = next

from typing import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.store = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store.keys():
            self.store.move_to_end(key)
            return self.store[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store.keys():
            self.store.move_to_end(key)
        self.store[key] = value
        if len(self.store) > self.capacity:
            self.store.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4