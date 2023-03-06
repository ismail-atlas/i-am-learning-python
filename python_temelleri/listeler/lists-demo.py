# 1
telefonlar = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

sonuc = telefonlar
sonuc = type(telefonlar)

# 2
sonuc = len(telefonlar)

# 3
sonuc = telefonlar[0]
sonuc = telefonlar[-1]

# 4
# telefonlar[0] = "Samsung S9"
sonuc = telefonlar

# 5
"""
if "Samsung S6" in telefonlar:
    print("ürün listenin bir elemanıdır.")
"""

# 6
sonuc = telefonlar[-3]

# 7
sonuc = telefonlar[:2]

# 8
# telefonlar[-2] = "Samsung S9"
# telefonlar[-1] = "Samsung S10"
sonuc = telefonlar

# 9
sonuc = telefonlar + ["IPhone X", "IPhone XR"]

# 10
# del telefonlar[-1]
sonuc = telefonlar

# 11
sonuc = telefonlar[::-1]

# 12
kullaniciA = ['Yiğit','Bilgi',2010,[70,60,70]]
kullaniciB = ['Sena','Turan',1999,[80,80,70]]
kullaniciC = ['Ahmet','Turan',1998,[80,70,90]]

ogrenciler = [kullaniciA,kullaniciB,kullaniciC]

for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2023-ogrenci[2]
    ortalama = round((ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) / 3)
    print(f"{ad} {soyad} {yas} {ortalama}")

# print(ogrenciler)

# 13
"""
for a in telefonlar:
    print(a)
"""

 # print(sonuc)