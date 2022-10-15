def val(v):
    f=0
    for i in range(len(v)):
        f+=ord(v[i])
    return f
def reverse(v):
    #print(s)
    temp=""
    f=0
    for i in range(len(v)):
        temp+=v[i]
        f+=ord(v[i])
    temp=''.join(sorted(temp))
    temp=str(temp)
    return temp
s=input()
z=""
c=s.split()
for i in range(len(c)-1):
    if len(c[i])<len(c[i+1]):
        continue
    elif len(c[i])>len(c[i+1]):
        temp=c[i]
        c[i]=c[i+1]
        c[i+1]=temp
    else :
        if(val(c[i])==val(c[i+1])):
            c[i]=reverse(c[i])
            c[i+1]=reverse(c[i+1])
        if (val(c[i])>val(c[i+1])):
            temp=c[i]
            c[i]=reverse(c[i+1])
            c[i+1]=reverse(temp)
print(*c)