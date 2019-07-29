h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if (h1>h2):
    hr=h1-h2
else:
    hr=h2-h1
if  (m1>m2):
    mn=m1-m2
else:
    mn=m2-m1
print(hr,mn)
