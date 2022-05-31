a=input()
arr=list(a.split())
##print(arr)
vo='aeiouAEIOU'
mi=100
fl=0
for i in (arr):
    c=0
    for j in i:
        if j in (vo):
            c+=1
            fl=1
    if(mi>c):
        mi=c
print(mi)

        