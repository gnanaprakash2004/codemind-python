n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1,-1,-1):
    if(a[i]==0 or a[i]==1):
        c+=1
if(c==n):
    print("True")
else:
    print("False")