class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x,y = abs(x) , abs(y)
        direction = {(1,2),(2,1),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)}
        q = collections.deque()
        visit = set()
        q.append((0,0,0))
        visit.add((0,0))
        while q:
            r,c,step = q.popleft()
            if (r,c) == (x,y):
                return step
            else:
                for i,j in direction:
                    nr,nc = r+i,c+j
                    if (nr,nc) not in visit and nr >= -2 and nc >= -2:
                        q.append((nr,nc,step+1))
                        visit.add((nr,nc))