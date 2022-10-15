n=input()
n=n.lower()
c=0
q=''
for i in n:
    if i not in q and n.count(i)==1 and i!=' ':
        q+=i
x="".join(sorted(q))
print(x)