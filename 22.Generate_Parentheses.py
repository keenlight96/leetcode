from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = 0
        c = 0
        string = []
        res = []
        self.add_parentheses(self, n, o, c, string, res)
        return res
        
    def add_parentheses(self, n, o, c, string: list, res: list):
        if len(string) == n * 2:
            res.append("".join(string))
        else:
            if o < n:
                string.append("(")
                self.add_parentheses(self, n, o + 1, c, string, res)
                string.pop()
            if c < o:
                string.append(")")
                self.add_parentheses(self, n, o, c + 1, string, res)
                string.pop()
solution = Solution
n = 1
print(solution.generateParenthesis(solution, n))