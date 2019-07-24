n=int(input())
c=[]
mul=n
for i in range (1,6):
    mul=n*i
    c.append(mul)
print(*c,sep=" ")
