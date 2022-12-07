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
if(prime(n)==0):
    print("Not Mega Prime")
else:
    
    temp=n
    z,c=0,0
    while(temp>0):
        z+=1
        r=temp%10
        if(prime(r)==1):
            c+=1
        else:
            c+=0
        temp=temp//10
    if(z==c):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
        