n=int(input())
for i in range (n):
    s=str(input())
    sr=str(s)[::-1]
    if(s==sr):
        if(len(s)%2==0):
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print("NO")
    #print(len(sr),len(s))
        