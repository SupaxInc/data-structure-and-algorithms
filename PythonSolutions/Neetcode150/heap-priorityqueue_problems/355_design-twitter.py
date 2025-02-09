class Twitter:

    def __init__(self):
        # Tracks the users following
        self.followingMap = defaultdict(set)
        # Tracks each users tweet
        self.tweetMap = defaultdict(list) # Pairs of [-time, tweetId]
        # Timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])

        # Decerement the time since the time will be used as the first value in the max heap
            # We are assuming here since posting tweet is synchronous that each posted tweet is an increment of time
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # A) Make user follow themselves so they can see their own recent tweets
        self.followingMap[userId].add(userId)

        # B) Grab the first recent tweet for EACH user that the current user is following
            # Allows us to know amongst which user being followed has the most recent tweet using a heap
        for followingId in self.followingMap[userId]:
            # Check if user has tweets, grab the latest tweet
            if followingId in self.tweetMap:
                latestTweetIdx = len(self.tweetMap[followingId]) - 1
                time, tweetId = self.tweetMap[followingId][latestTweetIdx]
                # Decrement latest tweet idx so we can get the next latest tweet below
                heapq.heappush(maxHeap, (time, latestTweetIdx - 1, tweetId, followingId))
        
        # C) Start adding the most recent tweets to result using the timestamp added to heap
            # If heap is empty, no more tweets have been found
        while maxHeap and len(res) < 10:
            time, latestTweetIdx, tweetId, followingId = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Check if the user has more tweets left by using the users tweet map list index
                # If its greater than or equal to 0 then that means there are more in the list
            if latestTweetIdx >= 0:
                time, tweetId = self.tweetMap[followingId][latestTweetIdx]
                # Decrement the index to get the next latest tweet for next iteration
                heapq.heappush(maxHeap, (time, latestTweetIdx-1, tweetId, followingId))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # First check if the followee is part of the users following list
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)