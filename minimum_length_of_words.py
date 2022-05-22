n=input()
arr=list(n.split())
mi=100
for i in arr:
    c=0
    for j in i:
        c+=1
    if c<mi:
        mi=c
    print(mi)
    break