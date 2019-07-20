a,b=map(int,input().split())
c=[]
for i in range(a,b):
    if(i%2==0):
     c.append(i)
for i in c:
    if(i==a) or (i==b):
        c.remove(i)
print(*c,sep=" ")
