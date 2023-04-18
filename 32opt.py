class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        maxSoFar = 0
        prev = 0 
        concat = False

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if not stack:
                    concat = False
                    continue

                rec = 2 + stack.pop()
                maxSoFar = max(maxSoFar,rec)
                
                if stack:
                    stack[-1] += rec
                    maxSoFar = max(maxSoFar,stack[-1])
                else:
                    if concat:
                        rec += prev
                        maxSoFar = max(maxSoFar,rec)

                    concat = True
                    prev = rec
        return maxSoFar
