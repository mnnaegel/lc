# naive O(n^2) solution but it works

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        memo = 3*(10**4)
        def greedy(beginIdx: int):
            if len(s) > (memo // 2):
                return 0
            stack = []
            checkPoint = 0
            for i in range(beginIdx, len(s)):
                if s[i] == '(':
                    stack.append('(')
                else:
                    if stack:
                        stack.pop()
                        if not stack:
                            checkPoint = (i-beginIdx)+1
                    else:
                        return checkPoint
            if not stack:
                checkPoint = ((len(s)-1)-beginIdx)+1
            return checkPoint
        
        maxSoFar = 0
        for i in range(len(s)):
            maxSoFar = max(maxSoFar,greedy(i))
        return maxSoFar

