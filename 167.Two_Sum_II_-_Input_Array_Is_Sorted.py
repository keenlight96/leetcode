from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while (sum:= numbers[left] + numbers[right]) != target:
            if sum > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
        
s = Solution()
numbers = [-1, 0]
target = -1
print(s.twoSum(numbers, target))