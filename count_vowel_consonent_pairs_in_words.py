n=input()
n=n.lower()
n=n.split()
v="aeiou"
c=0
for x in n:
    i=0
    j=len(x)-1
    while i<=j:
        if x[i] in v and x[j] not in v:
            c+=1
        elif x[i] not in v and x[j] in v:
            c+=1
        i+=1
        j-=1
print(c)