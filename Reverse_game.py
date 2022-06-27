n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    z=str(a[i])[::-1]
    print(int(z),end=' ')