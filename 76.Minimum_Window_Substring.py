from collections import Counter, defaultdict
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for x in t:
            if x not in d:
                d[x] = 0
            d[x] += 1
        l = m = r = 0
        sub = []
        min_sub = ""
        while r < len(s):
            if s[r] not in d:
                if not sub:
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                sub.append(r)
                d[s[r]] -= 1
                while d[s[sub[0]]] < 0:
                    d[s[sub[0]]] += 1
                    sub = sub[1:]
                    l = sub[0]
                if max(d.values()) == 0:
                    if not min_sub or len(min_sub) > len(s[sub[0]:sub[-1]+1]):
                        min_sub = s[sub[0]:sub[-1]+1]
                r += 1
        return min_sub
    
    def minWindow_optimize(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        m = [0] * 128
        for x in t:
            m[ord(x)] += 1
        l = r = 0
        sub = []
        min_sub = ""
        while r < len(s):
            if s[r] not in t:
                if not sub:
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                sub.append(r)
                m[ord(s[r])] -= 1
                while m[ord(s[sub[0]])] < 0:
                    m[ord(s[sub[0]])] += 1
                    sub = sub[1:]
                    l = sub[0]
                if max(m) == 0:
                    if not min_sub or len(min_sub) > len(s[sub[0]:sub[-1]+1]):
                        min_sub = s[sub[0]:sub[-1]+1]
                r += 1
        return min_sub
    
    def minWindow_performance(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needstr = collections.defaultdict(int)
        for ch in t:
            needstr[ch] += 1
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
                    
solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
s = "cabwefgewcwaefgcf" # "cwae"
t = "cae"
print(solution.minWindow_performance(s, t))