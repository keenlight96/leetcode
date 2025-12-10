from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = max(heights)
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                less = min(heights[i: j+1])
                area = less * (j + 1 - i)
                if area > res:
                    res = area
        return res
    
    def largestRectangleArea2(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for height in heights + [-1]:
            width = 0
            area = 0
            while stack and stack[-1][0] > height:
                h, w = stack.pop()
                width += w
                area = h * width
                res = max(res, area)
                
            stack.append([height, width + 1])
        return res
        
s = Solution()
heights = [2,1,3,4,2,3]
print(s.largestRectangleArea2(heights))
