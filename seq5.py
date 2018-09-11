"""seq5"""
def ses():
    """count 7 num ses print under"""
    num = int(input())
    ans = num
    for _ in range(7):
        if ans == 0:
            break
        else:
            print(ans, end=" ")
            ans -= 1
    print("")
    while ans > 0:
        for _ in range(7):
            if ans == 0:
                break
            else:
                print(ans, end=" ")
                ans -= 1
        print("")
ses()
                