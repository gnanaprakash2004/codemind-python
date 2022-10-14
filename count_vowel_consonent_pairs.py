n=input()
n=n.lower()
s=len(n)
v="aeiou"
i=0
j=s-1
c=0
while i<=j:
    if n[i]==' ' or n[j]==' ':
        i+=1
        j-=1
        continue
    elif n[i] in v and n[j] not in v:
        c+=1
    elif n[i] not in v and n[j] in v:
        c+=1
    i+=1
    j-=1
print(c)