x=input()
c=0
d=0
for i in (x):
    if i=='z':
        c=c+1
    else:
        d=d+1
    
if(c/d==1/2):
    print('Yes')
else:
    print('No')