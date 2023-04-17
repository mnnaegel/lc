from typing import List, Dict
from collections import defaultdict
from functools import cache

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # Construct the tree with the edges
        tree: Dict[int, List[int]] = defaultdict(list)
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        
        nodeTotalContribution: Dict[int, int] = defaultdict(int) # nodeTotalContribution[i] is the total contribution of node i across all trips
        
        visited = set()
        def dfs(node: int, target: int) -> bool:
            if node == target:
                nodeTotalContribution[node] += price[node]
                return True
            
            visited.add(node)
            for child in tree[node]:
                if child not in visited and dfs(child, target):
                    nodeTotalContribution[node] += price[node]
                    return True
            return False

        for trip in trips:
            visited = set()
            dfs(trip[0], trip[1])
        
        # Treat 0 as the root; find max depth and add each node to the bucket based on its depth
        nodesInDepth = defaultdict(list) # nodesInDepth[i] are nodes in the ith depth
        def traverse(node: int, depth: int, parent: int = None):
            nodesInDepth[depth].append(node)
            if len(tree[node]) == 1 and tree[node][0] == parent:
                return
                         
            for child in tree[node]:
                if child != parent:
                  traverse(child, depth + 1, node)
            return            
        traverse(0, 0)
        maxDepth = len(nodesInDepth) - 1
        
        totalContribution = 0
        for node in nodeTotalContribution:
            totalContribution += nodeTotalContribution[node]
        
        def computeCost(nodes: set) -> int:
            mytc = totalContribution
            for node in nodes:
                mytc -= nodeTotalContribution[node] // 2
            return mytc

        @cache
        def getOptimalNodes(root: int, parent: int) -> set:
            # print(">>>Root:", root, "Parent:", parent)
            optimalInSubtree = set()
            if (len(tree[root]) == 1 and tree[root][0] == parent) or len(tree[root]) == 0:
                optimalInSubtree.add(root)
                # print("Hit leaf", root, "Parent:", parent)
                return optimalInSubtree
            
            childrenContribution = 0
            for child in tree[root]:
                if child != parent and child in getOptimalNodes(child, root):
                  childrenContribution += nodeTotalContribution[child]
            
            os1 = set()
            os2 = set()
            os1.add(root)
            # union optimalInSubtree with root's children's children
            for child in tree[root]:
                if child == parent:
                    continue 
                    
                for grandchild in tree[child]:
                    if grandchild == child or grandchild == root:
                        continue
                    # print("gc:", grandchild, "c:", child, getOptimalNodes(grandchild, child))
                    os1 = os1.union(getOptimalNodes(grandchild, child))
              
            for child in tree[root]:
                if child != parent:
                    os2 = os2.union(getOptimalNodes(child, root))
            # print("Root:", root, "Parent:", parent, "Optimal:", optimalInSubtree) 

            if (computeCost(os1) > computeCost(os2)):
                return os2
            else:
                return os1
            
        optimalNodes = getOptimalNodes(0, None)
        print(optimalNodes)

        # recompute the total contribution of the optimal nodes, where if a node is optimal, then its contribution is halved
        return computeCost(optimalNodes)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTotalPrice(4,
[[0,1],[2,1],[1,3]],
[8,6,2,2],
[[3,3],[1,2],[0,3],[1,2],[2,0],[3,2],[0,2],[3,3],[0,2],[2,0],[1,2],[0,3],[3,1],[3,3],[2,2],[0,3],[0,2],[3,2],[1,0],[3,0],[3,1],[0,2],[3,1],[0,1],[2,1],[3,0],[1,2],[0,1],[1,0],[0,3],[1,2],[2,1],[3,2],[2,1],[2,0],[1,0],[3,0],[0,0],[0,3],[0,0],[3,0],[3,0],[1,3],[1,2],[0,3],[2,0],[0,3],[3,0],[0,2],[3,3],[0,2],[1,2],[0,0],[3,1],[3,0],[2,1],[3,1],[1,0],[1,2],[2,0],[3,3],[3,2],[2,0],[1,2],[1,2],[3,3],[0,2],[1,1],[0,0],[1,1],[3,0],[0,0],[1,1],[2,1],[3,1],[2,2],[0,2],[1,1],[1,3],[3,3],[1,2],[1,3],[0,2],[0,3],[2,3],[3,3],[3,3],[2,0],[3,2],[0,0],[1,2],[1,0],[2,3],[3,1]]))