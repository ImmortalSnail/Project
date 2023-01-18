n1,n2,n3,even = 0,1,0,0

while(n3 < 4000000):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 % 2 == 0:
        even += n3

print(even)