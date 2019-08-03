a=str(input())
arr=list(a)
count=0
for i in range(len(arr)):
    if(ord(a[i])==32):
        count+=1
print(count)
