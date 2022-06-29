n=int(input())
a=list(map(int,input().split()))
ar=[]
for i in a:
    if i not in ar:
        ar.append(i)
c=0
for i in ar:
    if i==a.count(i):
        c=1
        print(i,end=" ")
if c==0:
    print(-1)