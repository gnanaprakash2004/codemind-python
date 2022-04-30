import math
n=int(input())
m=n*n
temp=m
sum=0
while(temp>0):
    r=temp%10
    sum=sum+r
    temp=temp//10
if(sum==n):
    print('Neon Number')
else:
    print('Not Neon Number')