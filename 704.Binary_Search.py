from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        while nums[mid] != target:
            if nums[mid] > target:
                if nums[left] == target:
                    return left
                if mid == left:
                    return -1
                else:
                    right = mid
                    mid = (left + mid) // 2
            else:
                if nums[right] == target:
                    return right
                if mid == left:
                    return -1
                else:
                    left = mid
                    mid = int((mid + right) / 2)
        return mid
    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        return -1
    
solution = Solution()
nums = [-1,0,3,5,9,12]
target = 2
nums = [-1,0,5]
target = 5
print(solution.search2(nums, target))