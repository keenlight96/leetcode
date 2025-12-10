class Solution:
    def checkInclusion_bak(self, s1: str, s2: str) -> bool:
        set1 = set([s for s in s1])
        set2 = set1.copy()
        for s in s2:
            if s in set2:
                set2.remove(s)
                if not set2:
                    return True
            else:
                set2 = set1.copy()
        
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        l = r = 0
        for s in s1:
            dict1[s] = dict1[s] + 1 if s in dict1 else 1
            
        for r in range(len(s2)):
            if s2[r] not in dict1:
                dict1[s2[r]] = 0
            dict1[s2[r]] -= 1
            if max(dict1.values()) == min(dict1.values()) == 0:
                return True
            if min(dict1.values()) < 0:
                dict1[s2[l]] += 1
                l += 1
        return False
        
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))