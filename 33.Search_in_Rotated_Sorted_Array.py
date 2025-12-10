from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        side = 0
        while l <= r:
            if nums[m] == target:
                return m
            if target < nums[m]:
                if nums[m] >= nums[l]:
                    if target >= nums[l]:
                        side = 0
                    else:
                        side = 1
                else:
                    side = 0
            else:
                if nums[m] < nums[r]:
                    if target > nums[r]:
                        side = 0
                    else:
                        side = 1
                else:
                    side = 1
            if not side:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return -1

solution = Solution()
nums = [3,1]
target = 1
print(solution.search(nums, target))

assert solution.search(nums = [4,5,6,7,0,1,2], target = 0) == 4
assert solution.search(nums = [4,5,6,7,0,1,2], target = 3) == -1
assert solution.search(nums = [1], target = 0) == -1
assert solution.search(nums = [3,1], target = 1) == 1
print("Test OK")