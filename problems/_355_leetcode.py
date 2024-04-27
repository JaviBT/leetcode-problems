# 355. Design Twitter
# https://leetcode.com/problems/design-twitter

# Solution by: Javi Barranco

# Problem:
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.
# Implement the Twitter class:
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

# Example 1:
# Input:
#   ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
#   [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output:
#   [null, null, [5], null, null, [6, 5], null, [5]]

import heapq

class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        if userId in self.tweets:
            self.tweets[userId].append([-self.counter, tweetId])
        else:
            self.tweets[userId] = [[-self.counter, tweetId]]

    def getNewsFeed(self, userId: int) -> [int]:
        tweets = []
        
        followed_list = [userId] + (self.follows[userId] if userId in self.follows else [])

        for followee in followed_list:
            if followee in self.tweets:
                for tweet in self.tweets[followee]:
                    heapq.heappush(tweets, tweet)

        ret = []
        for _ in range(10):
            if tweets: ret.append(heapq.heappop(tweets)[1])
            else: break
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId not in self.follows[followerId]:
                self.follows[followerId].append(followeeId)
        else:
            self.follows[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)


exercise = Twitter()

input = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
params = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

expected_output = [None, None, [5], None, None, [6, 5], None, [5]]

output = [None]
for input, param in zip(input[1:], params[1:]):
    if input == 'getNewsFeed':
        output.append(exercise.getNewsFeed(*param))
    elif input == 'postTweet':
        output.append(exercise.postTweet(*param))
    elif input == 'follow':
        output.append(exercise.follow(*param))
    elif input == 'unfollow':
        output.append(exercise.unfollow(*param))
print(output)
for out, exp in zip(output, expected_output):
    assert out == exp, "Wrong answer"
print("Accepted")