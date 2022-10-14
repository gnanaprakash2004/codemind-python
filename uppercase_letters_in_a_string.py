s=list(map(str,input().split()))
c=0
a="QWERTYUIOPASDFGHJKLZXCVBNM"
for i in s:
    for j in i:
        if j in a:
            c+=1
print(c)