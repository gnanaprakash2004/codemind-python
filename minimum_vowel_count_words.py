s=list(map(str,input().split()))
mc=1000
v='aeiouAEIOU'
for i in s:
    vc=0
    for j in i:
        if j in v:
            vc+=1
    if vc<mc:
        mc=vc
c=0
for i in s:
    vc=0
    for j in i:
        if j in v:
            vc+=1
    if vc==mc:
        c+=1
print(c)