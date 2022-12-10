n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    x=int(a[i]**0.5)
    if(x*x==a[i]):
        c+=a[i]
print(c)