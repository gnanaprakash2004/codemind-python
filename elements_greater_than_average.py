n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1,-1,-1):
    s+=a[i]
av=s//n
c=0
for i in range(n):
    if(av<=a[i]):
        c+=1
print(c)