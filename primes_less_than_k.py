import math
def prime(n):
    if n==1:
        return 0
    else:
        for i in range(2,n):
            if(n%i==0):
                return 0
        else:
            return 1

n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
c=0
for i in range(n):
    if(prime(a[i])==1):
        b.append(a[i])
for i in range(len(b)):
    if(b[i]<=k):
        c+=1
print(c)