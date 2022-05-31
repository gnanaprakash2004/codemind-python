s1=str(input())
s2=str(input())
c=0
for i in s1.lower():
    if i in s2.lower():
        c+=1
    else:
        c+=0
if(c==len(s1) or c==len(s2)):
    print("True")
else:
    print("False")