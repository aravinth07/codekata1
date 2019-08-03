a=input()
li=['a','e','i','o','u','A','E','I','O','U']
if ord(a)>96 and ord(a)<123:
    if a in li:
        print("Vowel")
    else:
        print("Constant")
else:
    print("invalid")
