a=list(input())
c=[i for i in range(65,91)]
s=[i for i in range(97,123)]
n=[i for i in range(48,58)]
count=0
for i in range(len(a)):
    if ord(a[i]) not in c and ord(a[i]) not in s and ord(a[i]) not in n:
        count+=1
print(count)
