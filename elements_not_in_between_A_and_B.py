a=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
su=0
for i in arr:
    if(i<a or i>b):
        print(i,end=" ")
        su+=1
if su==0:
    print(-1)