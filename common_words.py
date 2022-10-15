s1=input()
s2=input()
u=s1.lower()
v=s2.lower()
r=u.split()
s=v.split()
for i in s:
    if i in r:
        print(i,end=' ')