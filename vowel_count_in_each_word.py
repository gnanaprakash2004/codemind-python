a=input()
arr=list(a.split())
vo='aeiouAEIOU'
for i in (arr):
    c=0
    for j in (i):
        if j in (vo):
            c+=1
    print(c,end=' ')