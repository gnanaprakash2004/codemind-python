n=input()
s=0
##print(n)
for i in n:
    if i in '0123456789':
        s+=ord(i)-48
print(s)