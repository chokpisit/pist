"""seq2"""
def ses():
    """num 1 3 5 7 9 ++"""
    num = int(input())
    ans = num*2
    num1 = 0
    for i in range(1, ans, 2):
       num1 += i
        print(num1, end=" ")
ses()
