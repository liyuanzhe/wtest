#coding=utf-8
# 计算用户平均转发、点赞、评论
from Feed import Feed

def increase_count(uid, uid_count_dict, delta):
        count = uid_count_dict.get(uid, 0)
        uid_count_dict[uid] = count + delta

def getBestFeed(feedList):
    maxScore = 0.0
    maxFeed = Feed("", -1, -2, -3)
    tmpDict = {}
    for feed in feedList:
        if(tmpDict.get(feed.getScore(), 0) == 1):
            continue
        else:
            tmpDict[feed.getScore()] = 1
        sumScore = 0.0
        for tmp in feedList:
            tmpScore = feed.calculateDelta(tmp)
            sumScore = sumScore + tmpScore
        if sumScore>maxScore:
            maxScore = sumScore
            maxFeed = feed
    return maxFeed

if __name__== "__main__":
    print("hello world")
    list = range(10)
    print(list)

    train_path = "/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/weibo_train_data.txt"
    pred_path = "/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/weibo_predict_data.txt"

    file = open(train_path)

    feed_dict = {}
    result_dict = {}

    # 读入数据
    while 1:
        line = file.readline()
        if not line:
            break

        arr = line.split("\t")
        if(len(arr) < 6):
            continue
        uid = arr[0]
        repost_count = int(arr[3])
        comment_count = int(arr[4])
        like_count = int(arr[5])

        feed = Feed(uid, int(repost_count), int(comment_count), int(like_count))
        feedList = feed_dict.get(uid, [])
        if(feedList == []):
            feedList.append(feed)
        else:
            feedList.append(feed)
        feed_dict[uid] = feedList

        pass

    print("read over")
    count = 0
    for uid in feed_dict.keys():
        feedList = feed_dict.get(uid, "0,0,0")
        result_dict[uid] = getBestFeed(feedList).getScore()
        count = count + 1
        if(count %100 == 0):
            print(count)

    print("calculate over")

    pred_file = open(pred_path)
    result_file = open("/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/result20171221.txt",'w')
    while 1:
        line = pred_file.readline()
        if not line:
            break

        arr = line.split("\t")
        uid = arr[0]
        mid = arr[1]
        result = result_dict.get(uid, "0,0,0")
        result_file.write(uid + "\t" + mid + "\t" + result + "\n")

        pass

    print("over")


