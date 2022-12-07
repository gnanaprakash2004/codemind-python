def prime(k):
    if k==0 or k==1:
        return 0
    else:
        for i in range(2,int(k**0.5)+1):
            if(k%i==0):
                return 0
                break
        return 1

n=int(input())
c=0
for i in range(1,n):
    for j in range(1,n):
        #print(i,j)
        x=prime(i)
        y=prime(j)
        if(x==1 and y==1):
            if(i*j==n):
                m=i
                n=j
                c+=1
                break
if(c==0):
    print(-1)
else:
    print(m,n)

