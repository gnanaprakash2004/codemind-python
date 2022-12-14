n=int(input())
l=list(map(int,input().split()))
b=[]
c=0
for i in range(n):
    if l[i]%2!=0:
        if l[i] not in b:
            b.append(l[i])
            c+=1
print(c)