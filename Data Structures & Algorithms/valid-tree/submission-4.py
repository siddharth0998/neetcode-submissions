class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        visit = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        return dfs(0,-1) and n == len(visit)
                
        