a=int(input())
b=[1,1]
for i in range(a-2):
    b.append(b[i]+b[i+1])
print(*b,sep=" ")
