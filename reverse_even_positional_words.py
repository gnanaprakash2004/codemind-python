s=input()
a=s.split()
for i in range(len(a)):
    if(i%2==0):
        print(str(a[i])[::-1],end=' ')
    else:
        print(a[i],end=' ')