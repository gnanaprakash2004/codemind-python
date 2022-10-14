a=list(map(str,input().split()))
c=0 
for s in a:
    
    s.lower()
    v=s[::-1]
    if v.lower()==s.lower() :
        c+=1
print(c)