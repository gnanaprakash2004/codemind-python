n=int(input())
a=list(map(int,input().split()))
e=[]
o=[]
for i in a:
    if i%2!=0:
        o.append(i)
    else:
        e.append(i)
#print(e,o)
i=0
while i<len(o) and i<len(e):
    print(o[i],e[i],end=" ")
    i+=1
j=i
while i<len(o):
    print(o[i],end=" ")
    i+=1
while j<len(e):
    print(e[j],end=" ")
    j+=1
if n%2!=0:
    print(0)