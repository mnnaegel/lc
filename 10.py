# beats 95% LOL

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        DOT = "."
        STAR = "*"

        def solve(s, p):
          slen = len(s)
          plen = len(p)
          pIdx = 0
          sIdx = 0
          while True:
              if (sIdx == slen and pIdx == plen):
                  return True
              
              if (sIdx != slen and pIdx == plen):
                  return False
              
              wasStar = False
              # check if next check if for a star character
              if (pIdx+1 < plen and p[pIdx+1] == STAR):
                  wasStar = True
                  # match as many characteres of p[idx] as possible
                  targ = p[pIdx] 
                  while True:
                      if sIdx == slen:
                          pi = pIdx 
                          if ((plen - pi) % 2 == 1):
                              return False

                          # next ensure that the last pairs of the chars in hte patter are in the form c*
                          while pi < plen-1:
                              if (p[pi+1] != STAR):
                                  return False
                              pi += 2
                          return True 
                      if targ != DOT and s[sIdx] != targ:
                          pIdx += 2
                          break
                      if solve(s[sIdx:], p[pIdx+2:]):
                        return True
                      sIdx += 1
                      

              if wasStar:
                  continue 
      
              # match p[i] with s[i]
              if (sIdx == slen or (p[pIdx] != DOT and p[pIdx] != s[sIdx])):
                  return False
              pIdx += 1
              sIdx += 1
          
        return solve(s,p)  