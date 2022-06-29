n=int(input())
a=list(map(int,input().split()))
k=int(input())
ar=0
for i in a:
    if(i<=k):
        ar+=i
print(ar)