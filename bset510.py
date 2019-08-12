n=int(input())
a=[i**2 for i in range(1,200)]
if n in a:
    print('yes')
else:
    print('no')
