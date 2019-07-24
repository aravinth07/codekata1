a,b=map(int,input().split())
c=[]
for num in range(a,b + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           c.append(num)
for i in c:
    if(i==a) or (i==b):
        c.remove(i)
print(*c,sep=" ")
