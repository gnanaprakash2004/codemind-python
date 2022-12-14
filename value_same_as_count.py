n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(n):
    if(l.count(l[i])==l[i]):
        if l[i] not in b:
            b.append(l[i])
print(len(b))