n=int(input())
lt1=[]
for i in range(n):
    lt1.append(input())

lt1.sort()
print(*lt1,sep=" ")
