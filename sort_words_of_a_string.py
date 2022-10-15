
def reverse(v):
    #print(s)
    temp=""
    f=0
    for i in range(len(v)):
        if v[i] >= 'a' and v[i] <= 'z' or v[i] >= 'A' and v[i] <= 'Z' and v[i]>='0' and v[i]<='9':
            temp+=v[i]
            f=1
    temp=''.join(sorted(temp))
    temp=str(temp)
    q=list(v)
    #print(q)
    x=0
    for i in range(len(q)):
        if q[i] >= 'a' and q[i] <= 'z' or q[i] >= 'A' and q[i] <= 'Z' and q[i]>='0' and q[i]<='9':
            q[i]=temp[x]
            x+=1
    u=""
    for i in range(len(q)):
        u+=q[i]
    return u
s=input()
z=""
c=s.split()
for i in range(len(c)):
    z+=reverse(c[i])
    if i+1<len(c):
        z+=' '
print(z)
    
	