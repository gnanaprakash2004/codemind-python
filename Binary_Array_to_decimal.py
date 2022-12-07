n=int(input())
a=list(map(int,input().split()))
s=0
p=n-1
for i in range(n):
    if(a[i]==1):
        s+=2**p
    p-=1
print(s)
        
    