from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def add_res(t: list):
            t = sorted(t)
            res.add(tuple(t))
            
        neg, pos = [], []
        zeros = 0
        res = set()
        for num in nums:
            if num == 0:
                zeros += 1
            elif num < 0:
                neg.insert(0, num)
            else:
                pos.append(num)
        NEG = set(neg)
        POS = set(pos)
        
        # Case (0,0,0)
        if zeros >= 3:
            add_res([0,0,0])
        
        # Case (0,x,y)
        if zeros > 0:
            for n in NEG:
                if -n in POS:
                    add_res([0,-n,n])
        
        # Case 2 neg 1 pos
        for i in range(len(neg) - 1):
            for j in range(i + 1, len(neg)):
                if -(neg[i] + neg[j]) in POS:
                    add_res([neg[i], neg[j], -(neg[i] + neg[j])])
        
        # Case 2 pos 1 neg
        for i in range(len(pos) - 1):
            for j in range(i + 1, len(pos)):
                if -(pos[i] + pos[j]) in NEG:
                    add_res([pos[i], pos[j], -(pos[i] + pos[j])])
        
        # Convert to list of lists
        res = [list(r) for r in res]
        return res
        
s = Solution()
# nums = [-1,0,1,2,-1,-4]
nums = [1,2,-2,-1]
print(s.threeSum(nums))