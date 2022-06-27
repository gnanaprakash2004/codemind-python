n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(n-1,-1,-1):
    s+=a[i]
av=s//n
for i in range(n):
    if a[i]<=av:
        c+=1
print(c)