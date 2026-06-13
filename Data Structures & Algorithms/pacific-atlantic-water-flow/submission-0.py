class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        q = collections.deque()
        visit = set()
        pacific = set()
        atlantic = set()
        for j in range(cols):
            q.append((0,j))
        for i in range(rows):
            q.append((i,0))
        while q:
            row,col = q.popleft()
            pacific.add((row,col))
            visit.add((row,col))
            for nr,nc in directions:
                r,c = row+nr,col+nc
                if (r in range(rows) and c in range(cols)
                    and (r,c) not in visit and heights[r][c] >= heights[row][col]):
                    visit.add((r,c))
                    q.append((r,c))
                    pacific.add((r,c))
        visit.clear()
        for i in range(rows):
            q.append((i,cols-1))
        for j in range(cols):
            q.append((rows-1,j))
        while q:
            row,col = q.popleft()
            atlantic.add((row,col))
            visit.add((row,col))
            for nr,nc in directions:
                r,c = row+nr,col+nc
                if (r in range(rows) and c in range(cols)
                    and (r,c) not in visit and heights[r][c] >= heights[row][col]):
                    visit.add((r,c))
                    q.append((r,c))
                    atlantic.add((r,c))
        return list(pacific & atlantic)