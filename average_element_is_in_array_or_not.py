n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range (n):
    sum+=arr[i]
avg=sum//n
c=0
for i in range (n):
    if(arr[i]==avg):
       c=1
       break
    else:
        c=0
if(c==1):
    print('True')
else:
    print('False')