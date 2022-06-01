n=input()
##arr=list(n.split())
vo='aeiouAEIOU'
di='1234567890'
ww=' '
v=c=d=w=0
for i in n:
        if i in vo:
            v+=1
        elif i not in vo and i not in di and i!=' ':
            c+=1
        elif i in di:
            d+=1
        elif i in ww:
            w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)