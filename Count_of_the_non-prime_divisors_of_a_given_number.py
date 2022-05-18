def prime(n):
    c=0
    if(n==1):
        return 1
    for i in range(2,n):
        if(n%i==0):
            return 1
    return 0
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(prime(i)==1):
            c+=1
print(c)