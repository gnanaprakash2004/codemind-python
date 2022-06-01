n=input()
c='abcdefghijklmnopqrstuvwxyz'
co=0
for i in n:
    for j in i.lower():
        if j not in c and j!=' ':
            co+=1
print(co)