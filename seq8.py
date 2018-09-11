"""seq8"""
def ses():
    """print
                  01
               01 02
            01 02 03
    """
    num = int(input())
    if 0 < num < 100:
        for i in range(1, num+1):
            ans1 = num-i
            print("   "*ans1, end="")
            for j in range(i):
                ans = j+1
                print("%02d" %ans, end=" ")
            print()
ses()
