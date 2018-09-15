"""seq7"""
def ses():
    """print 1-num slope and print num-1 - 1 slope"""
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        for _ in range(i):
            ans += 1
            print(ans, end=" ")
        ans = 0
        print("")
    for j in range(num-1, 0, -1):
        for _ in range(j):
            ans += 1
            print(ans, end=" ")
        ans = 0
        print("")
ses()
