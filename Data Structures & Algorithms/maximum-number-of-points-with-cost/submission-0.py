class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m , n = len(points), len(points[0])
        arr = points[0]

        for i in range(1,m):
            curr_arr = [0] * n
            left = [0] * n
            right = [0] * n
            left[0] = arr[0]
            for j in range(1,n):
                left[j] = max(left[j-1] - 1,arr[j])
            right[n-1] = arr[n-1]
            for j in range(n-2,-1,-1):
                right[j] = max(right[j+1] - 1,arr[j])
            for j in range(n):
                curr_arr[j] = max(left[j],right[j]) + points[i][j]
            arr = curr_arr
        return max(arr)