class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        while q:
            row,col,dis = q.popleft()
            for nr,nc in direction:
                r,c = row+nr,col+nc
                if (r in range(rows) and c in range(cols)
                and grid[r][c] != 0 and grid[r][c] != -1 and grid[r][c] > dis+1):
                    grid[r][c] = dis + 1
                    q.append((r,c,dis+1))
                            

