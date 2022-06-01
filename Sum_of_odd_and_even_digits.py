n=int(input())
arr=list(map(int,input().split()))
se=0
so=0
for i in range (n):
    if(i%2==0 or i==0):
        se+=arr[i]
    else:
        so+=arr[i]
if(so-se==0):
    print('YES')
else:
    print('NO')
    