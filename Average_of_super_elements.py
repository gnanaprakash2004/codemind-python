n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(n):
    if(l.count(l[i])==l[i]):
        #print(l[i])
        b.append(l[i])
if(len(b)==0):
    print(-1)
else:
        
    b=set(b)
    print('%.2f'%(sum(b)/len(b)))