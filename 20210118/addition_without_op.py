
a = 13
b = 15

while b!=0:
    carry = a & b
    print('{0:b}'.format(a), end= "->")
    print('{0:b}'.format(b), end= "->")
    print('{0:b}'.format(carry))
    a = a ^ b
    b = carry << 1


print('{0:b}'.format(a))


