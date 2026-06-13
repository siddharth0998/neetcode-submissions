class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0
        q = collections.deque()
        visit = set()
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    q.append((i,j))
                    res += 1
                    while q:
                        row,col = q.popleft()
                        for nr,nc in direction:
                            r,c = row + nr,col + nc
                            if (r in range(rows) and c in range(cols)
                                and (r,c) not in visit and grid[r][c] == "1"):
                                q.append((r,c))
                                visit.add((r,c))

        return res