n=str(input())
c=0
for i in n:
    if i in '0123456789':
        c+=1
    else:
        c+=0
if(c==0):
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")