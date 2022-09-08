n=int(input())
a=list(map(int,input().split()))
#print(a)
c=[]
for i in range(n):
    for j in range(n):
            if a[i] not in c:
                c.append(a[i])
print(*c)
            