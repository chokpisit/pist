"""seq4"""
def sess():
    """num**2 print row ses"""
    num = int(input())
    ses = 0
    for _ in range(num):
        for _ in range(num):
            ses += 1
            print(ses, end=" ")
        print("")
sess()
