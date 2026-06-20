class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [[0,0]] * (len(points))
        res = []
        for p in range(len(points)):
            i,j = points[p][0],points[p][1]
            dis = (i-0)**2 + (j-0)**2
            arr[p] = [dis,p]
            
        mod_arr = [[-x,idx] for x,idx in arr]
        heapq.heapify(mod_arr)
        while len(mod_arr) > k:
            heapq.heappop(mod_arr)
        while mod_arr:
            res.append(points[heapq.heappop(mod_arr)[1]])
        return res
        