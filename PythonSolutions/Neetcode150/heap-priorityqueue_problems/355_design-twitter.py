class Twitter:

    def __init__(self):
        self.count = 0
        self.followerMap = defaultdict(set) 
        self.tweetMap = defaultdict(list) # Pair of [count, tweetId]

    # Pretend that the user will always exist
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # Decrement since its a max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        # Make user follow themselves so we can see their own recent tweets
        self.followerMap[userId].add(userId)

        # Do a first run at grabbing recent tweets for each follower
        # Gives us the reference to the tweetmap for each user since we have the following id and the last index
        for followingId in self.followerMap[userId]:
            if followingId in self.tweetMap:
                lastIndex = len(self.tweetMap[followingId]) - 1
                count, tweetId = self.tweetMap[followingId][lastIndex] # Get most recent tweet
                # Add following id and last index to heap so we can traverse and find next recent tweets later
                # Decrement last index again to get next recent tweet
                heapq.heappush(maxHeap, [count, tweetId, followingId, lastIndex - 1])
        
        # Keep looking for the most recent tweets until result is 10
        # If max heap is empty that means there was only less than 10 tweets
        while maxHeap and len(res) < 10:
            # Max heap will give us the most recent tweet first using the count (timestamp)
            count, tweetId, followingId, lastIndex = heapq.heappop(maxHeap)
            # Add recent tweet to result
            res.append(tweetId)

            # Grab next recent tweet for the user id if they have more tweets
            if lastIndex >= 0:
                count, tweetId = self.tweetMap[followingId][lastIndex]
                heapq.heappush(maxHeap, [count, tweetId, followingId, lastIndex - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)