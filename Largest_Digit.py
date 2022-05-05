n=int(input())
ma=0
while n>0:
    r=n%10
    if(r>ma):
        ma=r
    else:
        ma=ma
    n=n//10
print(ma)