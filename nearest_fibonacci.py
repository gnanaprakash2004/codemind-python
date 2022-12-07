def nearfb(n):
    if(n==0):
        print(0)
        return
    else:
        f=0
        s=1
        t=s+f
        while(t<=n):
            f=s
            s=t
            t=f+s
        if(abs(t-n)>abs(s-n)):
            ans=s
        elif(abs(t-n)==abs(s-n)):
            print(s,t)
        else:
            ans=t
        print(ans)
        



n=int(input())
nearfb(n)