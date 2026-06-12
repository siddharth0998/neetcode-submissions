class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDia = set() # (r+c)
        negDia = set() # (r-c)
        board = [["."] * n for i in range(n)]
        def backTrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in posDia or (r-c) in negDia:
                    continue
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = "Q"
                backTrack(r+1)
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = "."
        backTrack(0)
        return res