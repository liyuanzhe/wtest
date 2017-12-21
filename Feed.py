class Feed(object):

    def __init__(self, uid, repostNum, commentNum, likeNum):
        self.uid = uid
        self.repostNum = repostNum
        self.commentNum = commentNum
        self.likeNum = likeNum

    def sum(self):
        return self.repostNum + self.commentNum + self.likeNum

    def printFeed(self):
        print('%s %s %s %s' % (self.uid, self.repostNum, self.commentNum, self.likeNum))

    def getScore(self):
        return "%s,%s,%s" % (self.repostNum, self.commentNum, self.likeNum)

    def isEqual(self, feed):
        return self.repostNum == feed.repostNum & self.commentNum == feed.commentNum & self.likeNum == feed.likeNum

    def calculateDelta(self, realFeed):
        deltaRepost = abs(self.repostNum - realFeed.repostNum)*1.0/(realFeed.repostNum + 5)
        deltaComment = abs(self.commentNum - realFeed.commentNum) * 1.0 / (realFeed.commentNum + 2)
        deltaLike = abs(self.likeNum - realFeed.likeNum) * 1.0 / (realFeed.likeNum + 3)
        precision = 1 - 0.5 * deltaRepost - 0.25 * deltaComment - 0.25 * deltaLike
        if(precision <= 0.8):
            return 0.0
        else:
            return (realFeed.sum() + 1)

