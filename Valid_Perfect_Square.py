import math
n=int(input())
for i in range (n):
    c=int(input())
    a=int(math.sqrt(c))
    if(a*a==c):
        print("True")
    else:
        print("False")
    