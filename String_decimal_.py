n=int(input())

for i in range (n):
    s=str(input())
    l=len(s)
    c=0
    for i in s:
        if i.isdigit():
            c+=1
        else:
            c+=0
    if(c==l):
        print("True")
    else:
        print("False")