s=list(map(str,input().split()))
a="qwertyuiopasdfghjklzxcvbnm"
c=0
for i in s:
    for j in i:
        if j in a:
            c+=1
print(c)