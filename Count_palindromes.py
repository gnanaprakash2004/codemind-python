n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range (n):
    z=str(arr[i])
    m=int(z[::-1])
    ##print(m)
    if(m==arr[i]):
        c+=1
    else:
        c+=0
print(c)