class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = collections.deque()
        visit = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visit:
                    visit.add((i,j))
                    count_v = 0
                    count_wv = 0
                    for s in range(m):
                        if s != i and grid[s][j] == 1:
                            if (s,j) in visit:
                                count_v += 1
                            else:
                                count_wv += 1
                                visit.add((s,j))
                    for t in range(n):
                        if t != j and grid[i][t] == 1:
                            if (i,t) in visit:
                                count_v += 1
                            else:
                                count_wv += 1
                                visit.add((i,t))
                    if count_wv != 0 or count_v != 0:
                        ans += 1 + count_wv
        return ans





                            