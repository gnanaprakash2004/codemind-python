n=int(input())
a=list(map(int,input().split()))
j=0
s=0
for i in range(n-1,-1,-1):
    s+=a[i]*(2**j)
    j+=1
print(s)