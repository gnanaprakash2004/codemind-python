n=int(input())
m=int(input())
for i in range (n,m+1):
    temp=i
    co=0
    c=0
    while(temp>0):
        r=temp%10
        co+=1
        if(r==0):
            break
        elif(i%r==0):
            c+=1
        temp//=10
    if(c==co):
        print(i,end=' ')