s=input()
a=s.split()
for i in a:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    print(c,end=" ")
        
