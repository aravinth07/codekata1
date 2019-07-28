n,s,d=map(int,input().split())
tot=0
val=s
for i in range(n):
    tot=tot+val
    val=val+d
print(tot)
