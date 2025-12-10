from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        de = deque()
        for i in range(len(nums)):
            while de and i - de[0] >= k:
                de.popleft()
            while de and nums[de[-1]] < nums[i]:
                de.pop()
            if i >= k - 1:
                if not de or nums[i] >= nums[de[0]]:
                    res.append(nums[i])
                else:
                    res.append(nums[de[0]])
            de.append(i)
        return res

solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
nums = [1,3,1,2,0,5]
k = 3
print(solution.maxSlidingWindow(nums, k))