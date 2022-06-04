n=int(input())
c=0
for i in range (n):
    s=str(input())
    c=0
    for i in s:
        if i.isdigit():
            c+=1
        else:
            c+=0
    if(c==0):
        print("No")
    else:
        print("Yes")
    
        