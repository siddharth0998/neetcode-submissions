class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        q = collections.deque()
        visit = set()
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        while q:
            row,col,min = q.popleft()
            for nr,nc in directions:
                r,c = row + nr,col + nc
                if (r in range(rows) and c in range(cols)
                    and (r,c) not in visit and grid[r][c] == 1):
                    q.append((r,c,min+1))
                    ans = max(ans,min+1)
                    visit.add((r,c))

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 1:
                    return -1
        return ans



