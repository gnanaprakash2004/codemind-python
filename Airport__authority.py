n=int(input())
p=[]
s=0
for i in range(n):
    v=int(input())
    p.append(v)
t=int(input())  
for i in range(n):
    if(p[i]>t):
        s+=2;
    else:
        s+=1;
print(s)