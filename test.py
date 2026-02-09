from collections import deque


arr = [1,2,3,4]
arr2 = deque(arr)
arr2.appendleft(0)
print(arr2)