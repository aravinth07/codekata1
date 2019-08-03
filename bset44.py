a=input()
b=list(a)
c=1
for i in range(len(b)):
    if ord(b[i])==46:
        c+=1
print(c)
