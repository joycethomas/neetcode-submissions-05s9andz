class Twitter:

    def __init__(self):
        #self.userID = None
        #self.followers = {} #should contain the user ids too 
        self.following = {}
        #newsFeed only has to be of size ten kinda, but it also has to keep things in order
        self.count = 0
        self.tweets = []
        heapq.heapify(self.tweets)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = {userId}
        self.count += 1
        heapq.heappush(self.tweets, (-1 * self.count, userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.following)
        #print(self.tweets)
        vis = []
        res = []
        followlist = self.following.get(userId)
        #print(userId, followlist)
        #problem is i'm getting their follower's post, not the people they're following

        while self.tweets:
            time, user, tweet = heapq.heappop(self.tweets)
            vis.append((time, user, tweet))
            if user in followlist:
                res.append(tweet)
                if len(res) == 10:
                    break
        for x in vis:
            heapq.heappush(self.tweets, x)
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        #if user 1 follows user 2
        #self.followers[user2] should have user1
        #user1 = followerId
        #user2 = followeeId
        '''if followerId not in self.followers:
            self.followers[followerId] = {followerId}
        if followeeId not in self.followers:
            self.followers[followeeId] = {followeeId}
        self.followers[followeeId].add(followerId)'''
        
        if followerId not in self.following:
            self.following[followerId] = {followerId}
        if followeeId not in self.following:
            self.following[followeeId] = {followeeId}
        self.following[followerId].add(followeeId)
        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if user 1 UNfollows user 2
        #self.followers[user2] should REMOVE user1
        #user1 = followerId
        #user2 = followeeId
        '''if followerId not in self.followers:
            self.followers[followerId] = {followerId}
        if followeeId not in self.followers:
            self.followers[followeeId] = {followeeId}
        self.followers[followeeId].remove(followerId)'''

        if followerId not in self.following:
            self.following[followerId] = {followerId}
        if followeeId not in self.following:
            self.following[followeeId] = {followeeId}
        if followeeId == followerId:
            return
        self.following[followerId].discard(followeeId)