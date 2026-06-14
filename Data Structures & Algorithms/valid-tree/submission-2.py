class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        visit = set()
        parent = {0:None}
        q = collections.deque()
        ans = 1

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q.append(0)
        while q:
            node = q.popleft()
            visit.add(node)
            for nei in adj[node]:
                if nei == parent.get(node):
                    continue
                if nei in visit:
                    return False
                parent[nei] = node
                visit.add(nei)
                ans += 1
                q.append(nei)

        return ans == n
                
        