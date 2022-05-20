n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    temp=arr[i]
    while temp>0:
        r=temp%10
        s+=r
        temp//=10
print(s)