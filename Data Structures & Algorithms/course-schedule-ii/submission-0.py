class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        inDegree = [0] * numCourses
        q = collections.deque()
        ans = []
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            inDegree[prerequisites[i][0]] += 1

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            ind = q.popleft()
            ans.append(ind)
            for nei in adj[ind]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return ans if len(ans) == numCourses else []