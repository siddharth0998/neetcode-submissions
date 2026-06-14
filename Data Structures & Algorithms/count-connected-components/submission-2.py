class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visit = set()
        q = deque()
        ans = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            if i in visit:
                continue
            ans += 1
            q.append(i)
            visit.add(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
        return ans