a=int(input())
arr=list(map(int,input().split()))
m=c=mc=0
for i in range(a):
    c=1
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                c+=1
    if c==mc:
        mc=c
        if arr[i]<m:
            m=arr[i]
    elif c>mc:
        mc=c
        m=arr[i]
print(m)