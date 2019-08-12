a,b=input().split()
a1=list(a)
b1=list(b)
c1=0
c2=0
for i in range(len(a1)):
    c1+=ord(a1[i])
    c2+=ord(b1[i])
if c1>=c2:
    m=a
else:
    m=b
print(m)
