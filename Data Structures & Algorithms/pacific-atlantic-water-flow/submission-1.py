class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pacific,atlantic = set(),set()
        def dfs(r,c,visit,prevHeight):
            if (r not in range(rows) or c not in range(cols)
                or (r,c) in visit or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for i in range(rows):
            dfs(i,0,pacific,heights[i][0])
            dfs(i,cols-1,atlantic,heights[i][cols-1])
        for j in range(cols):
            dfs(0,j,pacific,heights[0][j])
            dfs(rows-1,j,atlantic,heights[rows-1][j])
        return list(pacific & atlantic)