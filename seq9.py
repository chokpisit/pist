"""seq9"""
def ses():
    """
    input leg (0 < leg < 1000)
    print
          01
       01 02 01
    01 02 03 02 01
    """
    num = int(input())
    if 0 < num < 100:
        for i in range(1, num+1):
            ans1 = num-i
            print("   "*ans1, end="")
            for j in range(i):
                ans = j+1
                print("%02d" %ans, end=" ")
            for k in range(i, 1, -1):
                ans2 = k-1
                print("%02d" %ans2, end=" ")
            print()
ses()
