s=input()
e=str(input())
a=s.split()
c=0
for i in s:
    c+=1
    if(i==e):
        print("True")
        print(c-1)
        break
else:
    print("False")
    