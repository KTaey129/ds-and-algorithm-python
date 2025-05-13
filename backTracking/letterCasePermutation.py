# https://leetcode.com/problems/letter-case-permutation/description/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        
        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())
            else:
                for o in output:
                    tmp.append(o + c)
            output = tmp

        return output

  class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        res = []
        backtrack()
        return res
