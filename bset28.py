x,y=map(int,input().split())
c=[]
for i in range (x,y+1):
    a = 0
    t = i
    while t > 0:
        digit = t % 10
        a += digit ** 3
        t //= 10
    if i == a:
        if a!=y and a!=x:
            c.append(a)
print(*c,sep=" ")
