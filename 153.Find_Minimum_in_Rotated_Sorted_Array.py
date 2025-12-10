from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # edge case
        if nums[0] < nums[-1]:
            return nums[0]
        
        # normal cases
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        min = nums[m]
        while l <= r:
            if nums[m] < nums[-1]:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
            if nums[m] < min:
                min = nums[m]
        return min
    
solution = Solution()
nums = [3,4,5,1,2]
# print(solution.findMin(nums))
assert solution.findMin(nums = [3,4,5,1,2]) == 1
assert solution.findMin(nums = [4,5,6,7,0,1,2]) == 0
assert solution.findMin(nums = [11,13,15,17]) == 11
print("Test OK")