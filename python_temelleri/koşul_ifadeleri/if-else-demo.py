# 1
"""
sayi = int(input("sayı: "))

if 50 <= sayi <= 100:
    print("sayı 50 ve 100 arasındadır.")
else:
    print("sayı 50 ve 100 arasında değildir.")
"""

# 2
"""
sayi = int(input("sayı: "))

if (sayi > 0) and (sayi % 2 == 1):
    print("sayı pozitif tek sayıdır.")
elif (sayi > 0) and (sayi % 2 == 0):
    print("sayı pozitif ama tek değildir.")
elif (sayi < 0) and (sayi % 2 == 1):
    print("sayı tek ama negatiftir.")
else:
    print("sayı negatif ve tek değildir.")
"""

# 3
"""
_username = "ismailuludağ"
_password = "1234"

username = input("kullanıcı adı: ")
password = input("parola: ")

isusername = (_username == username)
ispassword = (_password == password)

if isusername:
    if ispassword:
        print("kullanıcı adı ve parola doğru!")
    else:
        print("parola yanlış!")
else:
    print("kullanıcı adı yanlış!")
"""

# 4
"""
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x>y) and (x>z):
    print("x en büyüktür.")
elif (y>x) and (y>z):
    print("y en büyüktür.")
else:
    print("z en büyüktür.")
"""

# 5

# vize1 = float(input("vize 1: "))
# vize2 = float(input("vize 2: "))
# final = float(input("final: "))

# ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)

# durum 1
"""
if (ortalama >= 50):
    print(f"öğrencinin not ortalaması: {ortalama} ve geçti.")
else:
    print(f"öğrencinin not ortalaması: {ortalama} ve kaldı.")
"""

# durum 2
"""
if (ortalama >= 50):
    if (final >= 50):
        print(f"öğrencinin not ortalaması: {ortalama} ve geçti.")
    else:
        print(f"öğrencinin not ortalaması: {ortalama} ve kaldı. Finalden en az 50 almalıdır.")
else:
    print(f"öğrencinin not ortalaması: {ortalama} ve kaldı.")
"""

# durum 3
"""
if (ortalama >= 50):
    print(f"öğrencinin not ortalaması: {ortalama} ve geçti.")
else:
    if (final >= 70):
        print(f"öğrencinin not ortalaması: {ortalama} ve öğrenci başarılı çünkü finalden 70 üstü aldı.")
    else:
        print(f"öğrencinin not ortalaması: {ortalama} ve kaldı.")
"""

# 6

ad = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))
 
kiloIndeks = kg / (hg ** 2)

if (kiloIndeks >= 0) and (kiloIndeks <= 18.4):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayıf.")
elif (kiloIndeks >= 18.5) and (kiloIndeks <= 24.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal.")
elif (kiloIndeks >= 25.0) and (kiloIndeks <= 29.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu.")
elif (kiloIndeks >= 30.0) and (kiloIndeks <= 34.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez.")
else:
    print("bilgileriniz yanlış.")