s=list(input())
c1=[i for i in range(97,123)]
c2=[i for i in range(65,91)]
n1=[i for i in range(48,57)]
c=0
n=0
for i in range(len(s)):
    if ord(s[i]) in c1 or ord(s[i]) in c2:
        c+=1
    if ord(s[i]) in n1:
        n+=1
if c>0 and n>0:
    print('Yes')
else:
    print('No')
