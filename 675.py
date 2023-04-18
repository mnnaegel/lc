# had to use function inlining to not TLE lol

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])

        movementArr = [(0,-1),(0,1),(1,0),(-1,0)]
        def bfs(coord1, target):
            q = deque()
            q.appendleft(coord1)
            visited = set()
            steps = 0
            while q:
                qsize = len(q)
                for i in range(qsize):
                    curr = q.popleft()
                    visited.add(curr)
                    
                    currY,currX = curr[0], curr[1]
                    if forest[currY][currX] == target:
                        return (curr, steps)
                    
                    for move in movementArr:
                        nextY, nextX = currY + move[0], currX + move[1]
                        nextCoord = (nextY, nextX)
                        if (nextY < 0 or nextY >= m or nextX < 0 or nextX >= n or forest[nextY][nextX] == 0):
                            continue

                        if nextCoord not in visited:
                            q.append(nextCoord)
                            visited.add(nextCoord)
                steps += 1
            return ((-1,-1),-1)

        
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    trees.append(forest[i][j])
        trees.sort()

        curr = (0,0)
        totalSteps = 0
        for i in range(len(trees)):
            curr, steps = bfs(curr, trees[i])
            if curr == (-1,-1): # didn't find target => graph is not connected
                return -1
            totalSteps += steps
        return totalSteps
