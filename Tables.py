m,n=map(int,input().split())
if(n>0):
    for i in range (1,n+1,2):
        print(m,'x',i ,'=',m*i)
else:
    for i in range (1,n+1,-2):
        print(m,'x',i ,'=',m*i)