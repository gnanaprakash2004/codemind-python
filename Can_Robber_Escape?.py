n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if arr[i]<n:
        c=1
    else:
        c=0
        break
if(c==0):
    print("NO")
else:
    print("YES")