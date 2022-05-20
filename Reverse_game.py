n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    m=str(arr[i])
    z=int(m[::-1])
    print(z,end=' ')