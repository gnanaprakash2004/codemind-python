n=int(input())
a=list(map(int,input().split()))
f,s=0,0
for i in range(n//2):
    f+=a[i]
for i in range((n//2),n):
    s+=a[i]
print(abs(f-s))