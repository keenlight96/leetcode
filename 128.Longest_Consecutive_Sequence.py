from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
                if count > max:
                    max = count 
            else:
                count = 1
        return max  
    

