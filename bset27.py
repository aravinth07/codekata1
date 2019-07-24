n = int(input())
a = 0
t = n
while t > 0:
   digit = t % 10
   a += digit ** 3
   t //= 10
if n == a:
   print("yes")
else:
   print("no")
