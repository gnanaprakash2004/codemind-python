n=int(input())
a=list(map(int,input().split()))
k=int(input())
ar=[]
for i in a:
    if i not in ar:
        ar.append(i)
c=0
for i in ar:
    if k==a.count(i):
        c=1
        print(i,end=" ")
if c==0:
    print(-1)