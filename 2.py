limit = 4000000

a = 1
b = 2
c = a + b
sum = b
while c < limit:
    if c % 2 == 0:
        sum += c
    a = b
    b = c
    c = a + b

print sum
