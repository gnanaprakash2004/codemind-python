s=input()
a=s.split()
for i in range(len(a)-1,-1,-1):
    print(str(a[i])[::-1],end=' ')