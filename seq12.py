"""
06                05 04 03 02 01      02 03 04 05 06
05 06                05 04 03 02      03 04 05 06        05
04 05 06                05 04 03      04 05 06        05 04
03 04 05 06                05 04      05 06        05 04 03
02 03 04 05 06                05      06        05 04 03 02
01 02 03 04 05 06                            05 04 03 02 01

02 03 04 05 06   05   06   05 04 03 02
03 04 05 06   05 04   05 06   05 04 03
04 05 06   05 04 03   04 05 06   05 04
05 06   05 04 03 02   03 04 05 06   05
06   05 04 03 02 01   02 03 04 05 06"""
def what():
    """p net """
    num = int(input())
    for i in range(1, num+1):
        for j in range(i):
            ans = num-i+1
            print("%02d" %(ans+j), end=" ")
        for k in range(num-i):
            print("%02d" %(num-k-1), end=" ")
        for jpg in range(num-i):
            print("%02d" %(jpg+1+i), end=" ")
        for jpg1 in range(i-1):
            print("%02d" %(num-jpg1-1), end=" ")
        print()
    for i in range(num, 1, -1):
        for jpg2 in range(i-1):
            ans1 = num-i+2
            print("%02d" %(ans1+jpg2), end=" ")
        for jpg3 in range(num-i+1):
            print("%02d" %(num-jpg3-1), end=" ")
        for jpg4 in range(num-i+1):
            print("%02d" %(jpg4+i), end=" ")
        for jpg5 in range(i-2):
            print("%02d" %(num-jpg5-1), end=" ")
        print()
what()
