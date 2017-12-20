#coding=utf-8
# 计算用户平均转发、点赞、评论


def increase_count(uid, uid_count_dict, delta):
        count = uid_count_dict.get(uid, 0)
        uid_count_dict[uid] = count + delta


if __name__== "__main__":
    print("hello world")
    list = range(10)
    print(list)

    train_path = "/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/weibo_train_data.txt"
    pred_path = "/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/weibo_predict_data.txt"

    file = open(train_path)

    line_count = 0
    uid_count_dict = {}
    uid_repost_dict = {}
    uid_like_dict = {}
    uid_comment_dict = {}
    result_dict = {}

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

        increase_count(uid, uid_count_dict, 1)
        increase_count(uid, uid_repost_dict, repost_count)
        increase_count(uid, uid_comment_dict, comment_count)
        increase_count(uid, uid_like_dict, like_count)

        line_count = line_count+1
        pass

    # 计算平均值
    for uid in uid_count_dict.keys():
        count = uid_count_dict[uid]
        avg_repost = uid_repost_dict[uid] * 1.0 / count
        avg_comment = uid_comment_dict[uid] * 1.0 / count
        avg_like = uid_like_dict[uid] * 1.0 / count
        result_str = str(int(avg_repost)) + "," + str(int(avg_comment)) + "," + str(int(avg_like))
        result_dict[uid] = result_str

    pred_file = open(pred_path)
    result_file = open("/home/liyuanzhe/Documents/tianchi/weibo/WeiboData/WeiboData/result.txt",'w')
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
    print(len(uid_like_dict.keys()))


