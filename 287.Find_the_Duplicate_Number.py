from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1 = set()
        for i in range(len(nums)):
            set1.add(nums[i])
            if len(set1) != i + 1:
                return nums[i]

s = Solution()
nums = [1,3,4,2,2]
print(s.findDuplicate(nums))