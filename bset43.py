l=str(input())
ar=list(l)
c=0
for i in range(len(ar)):
    if(ord(l[i])==32):
        c+=1
print(c)
