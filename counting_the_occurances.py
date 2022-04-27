x=input()
y=input()
c=0
for i in x:
    if(i==y):
        c=c+1
if c>0:
    print(c)
else:
    print('-1')