n=int(input())
arr=list(map(int,input().split()))
index=0
for i in range(n):
    if(arr[i]%2!=0):
        index=i
print(index)