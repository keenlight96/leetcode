from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idxes, res = [], []
        for i in range(len(temperatures)):
            while idxes and temperatures[idxes[-1]] < temperatures[i]:
                res[idxes[-1]] = i - idxes[-1]
                idxes.pop()
            
            idxes.append(i)
            res.append(0)
        return res

s = Solution()
temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]
print(s.dailyTemperatures(temperatures1))