s=list(map(str,input().split()))
a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321"
c=0
for i in s:
    for j in i:
        if j not in a:
            c+=1
print(c)