"""
01 01 01 01 01
01 02 02 02 01
01 02 03 02 01
01 02 02 02 01
01 01 01 01 01
"""
def ses():
    """thinking of you"""
    num = int(input())
    ans = -1*num
    for i in range(ans+1, num):
        for j in range(num-1, ans, -1):
            pri = num - max(abs(j), abs(i))
            print("%02d" %pri, end=" ")
        print()
ses()
