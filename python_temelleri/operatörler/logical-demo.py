# 1 
"""
sayi = int(input("sayı: "))

sonuc = (sayi >= 50) and (sayi <= 100)
"""

# 2
"""
sayi = int(input("sayı: "))

sonuc = (sayi > 0) and (sayi % 2 == 1)
print(sonuc)
"""

# 3
"""
adi = "ismail"
sifre ="12345"

username = input("ad: ")
parola = input("parola: ")

sonuc = (username.lower().strip() == adi) and (parola.strip() == sifre)

print(sonuc)
"""

# 4
"""
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

sonuc = (x>y) and (x>z) # x en büyük
print("x en büyük sayıdır: ", sonuc)

sonuc = (y>x) and (y>z) # y en büyük
print("y en büyük sayıdır: ", sonuc)

sonuc = (z>x) and (z>y) # z en büyük
print("z en büyük sayıdır: ", sonuc)
"""

# 5
"""
vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final: "))

ortalama = (((vize1 +vize2) / 2) * 0.6) + (final * 0.6)
# sonuc = (ortalama >= 50) and (final >= 50) 
sonuc = (ortalama >= 50) or (final >= 70)
print(f"öğrencinin not ortalaması: {ortalama} ve geçme durumu: {sonuc}")
"""

# 6

ad = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))
 
kiloIndeks = kg / (hg ** 2)

zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
normal = (kiloIndeks >= 18.5) and (kiloIndeks <= 24.9)
kilolu = (kiloIndeks >= 25.0) and (kiloIndeks <= 29.9)
obez = (kiloIndeks >= 30.0) and (kiloIndeks <= 34.9)

print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez: {obez}")