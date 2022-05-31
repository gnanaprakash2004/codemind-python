n=input()
v=input()
c=0
l=len(n)
for i in range(l):
    if(n[i]==v):
        print("True")
        print(i)
        break
else:
    print(False)

        