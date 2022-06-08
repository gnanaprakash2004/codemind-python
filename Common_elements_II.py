a,b=map(int,input().split())
ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
s=[]

for i in ar1:
    if i not in ar2:
        if i not in s:
            s.append(i)
        ##print((s))
for i in ar2:
    if i not in ar1:
        if i not in s:
            s.append(i)
print(*s)