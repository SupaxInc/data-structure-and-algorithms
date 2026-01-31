from collections import defaultdict, heapq
from typing import List
# Visualization
# user -> set(user)

# 1 -> (2)
# {
#     1 -> list[timestamp, tweetId]: [[1, 2], [4, 11]]
#     2 -> [[2, 6], [3, 10]]
# }

class Twitter:
    
    def __init__(self):
        self.followerMap: set(int) = defaultdict(set)
        self.tweetMap: List[int, int] = defaultdict(list) # [timestamp, tweetId]
        self.timestamp = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        self.tweetMap[userId].append([self.timestamp, tweetId])
    
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = [] # timestamp, tweetId, followerId, latestTweetIdx 
        res = []

        # Make the user follow themselves so we can add their own tweet to the newsfeed
        self.followerMap[userId].add(userId)

        # Only add the recent tweets for each of their followers, helps save space to prevent adding ALL users tweets in-memory
        for followerId in self.followerMap[userId]:
            followerTweets = self.tweetMap[followerId]
            # If the user has tweets
            if followerTweets:
                # The latest tweet index let us know if the user has more tweets AND the NEXT latest tweet
                latestTweetIdx = len(followerTweets) - 1
                timestamp, tweetId = followerTweets[latestTweetIdx]
                # Add the tweet + the users NEXT LATEST tweet index
                heapq.heappush(maxHeap, [timestamp, tweetId, followerId, latestTweetIdx - 1])
        
        while maxHeap and len(res) < 10:
            timestamp, tweetId, followerId, latestTweetIdx = heapq.heappop(maxHeap)
            res.append(tweetId)

            # Check if the user has more tweets so we can continually add more recent tweets per iteration
            if latestTweetIdx >= 0:
                # Get the users NEXT latest tweet
                newTimestamp, newTweetId = self.tweetMap[followerId][latestTweetIdx]
                # Decrement latest tweet index again to get next recent tweet
                heapq.heappush(maxHeap, [newTimestamp, newTweetId, followerId, latestTweetIdx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            # Use discard instead of remove in Python to prevent throwing an error when removing a value from a set that doesn't exist
            self.followerMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)