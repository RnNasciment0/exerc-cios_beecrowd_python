s = input().split()
a = int(s[0])
b = int(s[1])
if b < 0:
    b *= -1
    r = a % b
    q = a // b
    print(q * -1, r)
else:
    r = a % b
    q = a // b
    print(q, r)
