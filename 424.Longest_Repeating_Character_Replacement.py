class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_frequency = {}
        l = r = 0
        
        while r < len(s):
            if s[r] not in char_frequency.keys():
                char_frequency[s[r]] = 0
            char_frequency[s[r]] += 1
            
            if (r - l + 1 - max(char_frequency.values())) <= k:
                res = max(res, r - l + 1)
            else:
                char_frequency[s[l]] -= 1
                l += 1
            r += 1
        return res

solution = Solution()
s = "ABBB"
k = 2
print(solution.characterReplacement(s, k))