n=int(input())
a=list(map(int,input().split()))
c=0
for i in set(a):
    
    if(i==a.count(i)):
        c+=1
print(c)
