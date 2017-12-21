from Feed import Feed


if __name__== "__main__":
    print("hello")
    feed1 = Feed("1", int("3"), int("4"), int("5"))
    feed2 = Feed("2", int("3"), int("6"), int("7"))
    a = []
    print(a == [])
    a.append(feed1)
    print(a)
    feed1.printFeed()
    print(feed1.calculateDelta(feed2))
    print(feed1.getScore())
