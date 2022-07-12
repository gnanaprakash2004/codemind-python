s=input()
a='aeiou'
b=''
for i in s:
    if i in a:
        if i not in b:
            b+=i
        
if(len(b)==5):
    print("True")
else:
    print("False")
    