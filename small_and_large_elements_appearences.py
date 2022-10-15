n=input()
x=ord(n[0])
z=0
for i in range(1,len(n)):
    if n[i]!=' ':
        if (ord(n[i])<x):
            x=ord(n[i])
            z=i
q=n[z]
y=ord
r=0
for i in range(1,len(n)):
    if n[i]!=' ':
        if (ord(n[i])>x):
            x=ord(n[i])
            r=i
w=n[r]
print(q,n.count(q),w,n.count(w),end=' ')