n=int(input())
arr=list(map(int,input().split()))
o=0
e=0
for i in range (n):
    if arr[i]%2==0:
        e+=1
    else:
        o+=1
print(e,end=' ')
print(o,end=' ')