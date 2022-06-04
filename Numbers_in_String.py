n=input()
s=0
for i in n:
    if i.isdigit():
       c=ord(i)-48
       s+=c
print(s)