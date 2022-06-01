a=int(input())
for i in range (a):
    a,b=map(int,input().split())
    co=0
    for j in range(a,b+1):
        if j%10==2 or j%10==3 or j%10==9:
            co+=1
    print(co)