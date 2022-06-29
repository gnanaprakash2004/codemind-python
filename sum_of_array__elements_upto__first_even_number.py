n=int(input())
a=list(map(int,input().split()))
ar=0
for i in a:
    if(i%2==0):
        break
    ar+=i
print(ar)