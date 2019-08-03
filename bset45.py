a=input()
b=list(a)
c=0
for i in range(len(b)):
    for j in range(10):
        if ord(b[i])>47 and ord(b[i])<58:
            c+=1
c=int(c/10)
print(c)
