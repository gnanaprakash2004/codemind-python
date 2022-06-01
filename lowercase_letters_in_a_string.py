n=input()
lc='abcdefghijklmnopqrstuvwxyz'
c=0
for i in n:
    for j in i:
        if j in lc:
            c+=1
print(c)