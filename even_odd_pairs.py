n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i=0
while i<len(e) and i<len(o):
    print(e[i],o[i],end=" ")
    i+=1
j=i
while i<len(e):
    print(e[i],end=" ")
    i+=1
while j<len(o):
    print(o[i],end=" ")
    j+=1
if n%2!=0:
    print(0)