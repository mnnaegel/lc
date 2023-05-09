from typing import List 
from collections import defaultdict

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopesX = sorted(envelopes, key=lambda x: x[0])
        envelopesY = sorted(envelopes, key=lambda x: x[1])
        dp = defaultdict(set)

        firstXEnvelope = envelopesX[0]
        firstYEnvelope = envelopesY[0]
        
        dp[(firstYEnvelope[0], firstYEnvelope[1])] = 1
        dp[(firstXEnvelope[0], firstXEnvelope[1])] = 1

        minx = firstXEnvelope[0]
        miny = firstYEnvelope[1]

        
  

if __name__ == "__main__":
    s = Solution()
    print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))