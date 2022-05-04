import math
a,b,c=map(int,input().split())
d=math.pow(a,b)
print('%.0f'%(d%c))