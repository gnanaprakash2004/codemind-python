def col(l):
    m=sorted(l)
    n=sorted(l,reverse=True)
    return l==m or l==n
a,b=map(int,input().split())
mat=[]
for i in range(a):
    x=list(map(int,input().split()))
    mat.append(x)
cnt=0
for j in range(b):
    z=[]
    for i in range(a):
        z.append(mat[i][j])
    if col(z):
        cnt+=1
print(cnt)