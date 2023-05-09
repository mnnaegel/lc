class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def solve(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if word1[i] == word2[j]:
                return solve(i-1,j-1)

            insertionRes = 1+solve(i, j-1)
            deletionRes = 1+solve(i-1,j)
            replaceRes = 1+solve(i-1,j-1)
            return min(insertionRes, deletionRes, replaceRes)
        
        n = len(word1)
        m = len(word2)

        if not n:
            return m
        if not m:
            return n
        return solve(len(word1)-1, len(word2)-1)
