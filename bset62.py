n=int(input())
a={'One':1,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10}
for x,y in a.items():
    if y==n:
        print(x)
