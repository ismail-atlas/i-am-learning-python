x = 8

# 1- And (ve) Operatörü

# sonuc = 5 < x < 15
sonuc = (x > 5) and (x < 15) 

# True ve True => True
# False ve True => False
# False ve False => False

hak = 3
devam = "e"

sonuc = (hak > 0) and (devam == "e")

# or (veya) Operatörü

sonuc = (x > 0) or (x % 2 == 0) 
 
# True veya True => True
# False veya True => True
# False veya False => False

# not operatörü

sonuc = not(x > 0)


# x, 5-10 arasında bir çift sayı mı?

sonuc = ((x > 5) and (x < 10)) and (x%2==0)
print(sonuc)