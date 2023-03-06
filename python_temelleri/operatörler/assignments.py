# a = 5
# b = 10
# c = 20

a, b, c = 21, 10, 20

# a, b = b, a
a += 5        # a = a + 5
a -= 5        # a = a - 5
a *= 5        # a = a * 5
a /= 5        # a = a / 5
a %= 5        # a = a % 5
a **= 5        # a = a ** 5
a //= 5        # a = a // 5

# values = 1, 2             #    ValueError: not enough values to unpack (expected 3, got 2)
# values = 1, 2, 3, 4, 5      #    ValueError: too many values to unpack (expected 3)
values = (1, 2, 3, 4, 5)

# a, b, *c = values         #   1 2 [3, 4, 5]
a, *b, c = values           #   1 [2, 3, 4] 5
*a, b, c = values           #   [1, 2, 3] 4 5

sonuc = values

print(a,b,c)
print(sonuc)