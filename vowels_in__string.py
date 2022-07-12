s=input()
v='aeiouAEIOU'
m=''
for i in s:
    if i in v:
        if i not in m:
            m+=i
if(len(m)==0):
    print(0)
else:
    print(*m)
        
        