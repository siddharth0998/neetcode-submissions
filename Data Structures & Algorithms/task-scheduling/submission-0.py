class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                element = heapq.heappop(maxHeap)
                element += 1
                if element:
                    q.append([element,time+n])
            if q and q[0][1] == time:
                task,t = q.popleft()
                heapq.heappush(maxHeap,task)
        return time