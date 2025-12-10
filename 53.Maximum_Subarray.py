from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSub(nums, 0, len(nums) - 1)
    
    def maxLeft(self, nums, left, mid):
        max_sum = float("-inf")
        sum = 0
        for i in range(mid, left-1, -1):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum
    
    def maxRight(self, nums, mid, right):
        max_sum = float("-inf")
        sum = 0
        for i in range(mid, right+1, 1):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
        return max_sum
    
    def maxSub(self, nums, left, right):
        if left == right:
            return nums[left]
        
        mid = left + (right - left) // 2
        
        max_left = self.maxSub(nums, left, mid)
        max_right = self.maxSub(nums, mid + 1, right)
        max_mid = self.maxLeft(nums, left, mid) + self.maxRight(nums, mid + 1, right)
        return max(max_left, max_right, max_mid)

s = Solution()
nums = [5,4,-1,7,8]
print(s.maxSubArray(nums))