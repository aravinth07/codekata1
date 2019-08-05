a=list(input().split())
temp=a[0]
a[0]=a[1]
a[1]=temp
print(*a,sep=" ")
