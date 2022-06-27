n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    z=str(a[i])[::-1]
    if(int(z)==a[i]):
        c+=1
print(c)