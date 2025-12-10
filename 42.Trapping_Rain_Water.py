from typing import List


class Solution:
    def trap_bak(self, height: List[int]) -> int:
        total_area = 0
        area = 0
        left = 0
        right = 1
        while right < len(height):
            if height[right] < height[left]:
                area += height[left] - height[right]
            else:
                total_area += area
                left = right
                area = 0
            right += 1
        return total_area
    
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        area = 0
        
        while left < right:
            if left_max <= right_max:
                area += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                area += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return area
        

    def trap2(self, height: List[int]) -> int:
        i = 0
        left_max = height[0]
        sum = 0
        j = len(height) - 1
        right_max = height[j]
        while i < j:
            if left_max <= right_max:
                sum += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                sum += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
        return sum
    
s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))