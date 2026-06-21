class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[1] * (n) for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                arr[i][j] = arr[i][j+1] + arr[i+1][j]
        return arr[0][0]