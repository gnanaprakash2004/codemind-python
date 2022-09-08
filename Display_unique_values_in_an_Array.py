n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if(a.count(a[i])==1):
        b.append(a[i])
if(len(b)==0):
    print(-1)
else:
    print(*b)