list = []
prime_list = []
x = 600851475143
y = 2

while (x != 1):
    if (x % y == 0):
        x = x / y
        list.append(y)
    else:
        y += 1

