def ispalin(ss):
    return ss == ss[::-1]
    
s=str(input())
ss=s.lower()
ans=ispalin(ss)
if (ans):
    print("True")
else:
    print("False")
