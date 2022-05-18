def sample(n):
    if n==1:
        return 1
    else:
        return n*sample(n-1)
p=int(input())
for i in range (p):
    c=int(input())
    print(sample(c))