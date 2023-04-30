from typing import List

class UnionFind:
    def __init__(self, n):
        self.array = [-1 for _ in range(n)]
      
    def find(self, x):
        nodeStack = []

        while self.array[x] != -1:
            nodeStack.append(x)
            x = self.array[x]
          
        for node in nodeStack:
            self.array[node] = x

        return x
    
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return False
        self.array[yp] = xp
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        res = [False for _ in range(len(queries))]

        # sort edgeList by weight
        edgeList.sort(key=lambda x: x[2]) 

        # enumerate the queries to keep track of original ordering then sort them on the last element (weight) 
        for i, query in enumerate(queries):
            query.append(i)
        queries.sort(key=lambda x: x[2])

        edgeListIndex = 0
        # for query in queries:
        for query in queries:
            # while edgeListIndex < len(edgeList) and edgeList[edgeListIndex][2] < query[2]:
            while edgeListIndex < len(edgeList) and edgeList[edgeListIndex][2] < query[2]:
                uf.union(edgeList[edgeListIndex][0], edgeList[edgeListIndex][1])
                edgeListIndex += 1
            res[query[3]] = uf.find(query[0]) == uf.find(query[1])
        return res
            

# if name == main
if __name__ == "__main__":
    s = Solution()
    # n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
    print(s.distanceLimitedPathsExist(5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]]))