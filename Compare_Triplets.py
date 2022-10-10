n=3
p=list(map(int,input().split()))
q=list(map(int,input().split()))
alice=0
bob=0
for i in range(n):
    if(p[i]>q[i]):
        alice+=1
    elif(q[i]>p[i]):
        bob+=1
    else :
        continue
print(alice, bob)