s=input()
v='aeiou'
m=''
for i in s:
    if i in 'aeiou':
        if i not in m:
            m+=i
if(len(m)>=5):
    print(0)
for i in v:
    if i not in m:
        print(i,end=' ')
    
        

        