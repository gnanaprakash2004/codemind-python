n=int(input())
a=list(map(int,input().split()))
ar=[]
for i in a:
    if i not in ar:
        ar.append(i)
for i in ar:
    print(i,a.count(i),end=" ")