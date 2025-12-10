import math
from typing import List
import unittest

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        m = (l + r) // 2
        min_speed = r
        while l <= r:
            sum = 0
            for b in piles:
                sum += math.ceil(b / m)
            if sum <= h:
                if m < min_speed:
                    min_speed = m
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return min_speed

solution = Solution()
piles = [3,6,7,11]
h = 8

assert solution.minEatingSpeed(piles = [3,6,7,11], h = 8) == 4
assert solution.minEatingSpeed(piles = [30,11,23,4,20], h = 5) == 30
assert solution.minEatingSpeed(piles = [30,11,23,4,20], h = 6) == 23
print("Test OK")