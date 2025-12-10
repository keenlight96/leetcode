from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                maxP = max(maxP, prices[i] - buy)
        return maxP
        
s = Solution()
prices = [7,6,4,3,1]
print(s.maxProfit(prices))