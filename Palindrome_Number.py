a=int(input())
for i in range (a):
    n=int(input())
    temp=n
    rev=0
    while temp!=0:
        r=temp%10
        rev=rev*10+r
        temp//=10
    if(rev==n):
        print("True")
    else:
        print("False")