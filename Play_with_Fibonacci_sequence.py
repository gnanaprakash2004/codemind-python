def fibi(i):
    if n==1:
        print('0')
    elif n==2:
        print('0'+' '+'1')
    else:
        a,b=0,1
        print(a,b,end=' ')
        for i in range(2,n):
            c=a+b
            print(c,end=' ')
            a=b
            b=c
n=int(input())
fibi(n)