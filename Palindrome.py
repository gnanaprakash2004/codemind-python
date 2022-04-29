n=int(input())
temp=n
m=0
while (n>0):
    r=n%10
    m=m*10+r
    n=n//10
if m==temp:
    print('True')
else:
    print('False')
