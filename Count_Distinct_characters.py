n=input()
n=n.lower()
c=0
q=""
for i in n:
    if i not in q and i!=' ':
        q+=i
        c+=1
print(len(q))