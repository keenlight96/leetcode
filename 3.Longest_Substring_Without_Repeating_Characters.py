class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        string = ""
        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
                max_ = max(max_, len(string))
            else:
                string = string[string.find(s[i]) + 1:] + s[i]
        return max_
        
solution = Solution()
# s = "abcabcbb"
s = "ohvhjdml" # 6
print(solution.lengthOfLongestSubstring(s))