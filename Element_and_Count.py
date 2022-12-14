n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(n):
    if l[i] not in b:
        b.append(l[i])
        print(l[i],l.count(l[i]),end=' ')
    