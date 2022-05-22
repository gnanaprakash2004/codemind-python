a=input()
arr=list(a.split())
mx=0
for i in arr:
    c=0
    for j in i:
        c+=1
    if c>mx:
        mx=c
print(mx)
