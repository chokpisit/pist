"""Sequence I"""
def main():
    """input num"""
    num = int(input())
    for _ in range(num):
        for i in range(num):
            print(i+1, end=" ")
        print("")
main()
