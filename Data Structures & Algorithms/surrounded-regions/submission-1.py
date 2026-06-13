class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()
        q = collections.deque()
        for i in range(rows):
            if board[i][0] == "O": # capital alphabet O not zero
                q.append((i,0))
            if board[i][cols-1] == "O":
                q.append((i,cols-1))
        for j in range(cols):
            if board[0][j] == "O":
                q.append((0,j))
            if board[rows-1][j] == "O":
                q.append((rows-1,j))
        while q:
            row,col = q.popleft()
            visit.add((row,col))
            for nr,nc in directions:
                r,c = row+nr,col+nc
                if (r in range(rows) and c in range(cols)
                    and (r,c) not in visit and board[r][c] == "O"):
                    visit.add((r,c))
                    q.append((r,c))
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and board[i][j] == "O":
                    board[i][j] = "X"
