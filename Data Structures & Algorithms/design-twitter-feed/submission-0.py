class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) # userId -> set of followeeId
        self.tweets = defaultdict(list) # userId -> [[count,tweetId]]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count,tweetId = self.tweets[followeeId][index]
                minHeap.append([count,tweetId,followeeId,index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count,tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId,index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
