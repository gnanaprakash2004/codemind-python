n=input()
arr=list(n.split())
c=0
for i in arr:
    for j in i:
        if(j!=' '):
            c+=1
print(c)