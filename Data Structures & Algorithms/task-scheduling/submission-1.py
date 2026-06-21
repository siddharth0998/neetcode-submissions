"""
so basically we maintain one maxheap and one queue in maxheap we store
count of frequency of each character we take most frequency, decrement it
and store it's curr frequency with next available time stamp into
queue. we also maintain one variable call time,we keep poping from
maxheap and if curr time matches queues's first element time means
we have to add this element into maxheap again and pop from queue.
"""

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