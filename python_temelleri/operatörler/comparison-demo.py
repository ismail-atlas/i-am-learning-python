# 1 

# sayi1 = int(input("sayı 1: "))
# sayi2 = int(input("sayı 2: "))

# sonuc = (sayi1 > sayi2)
# print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")

# 2
"""
sayi = int(input("sayı: "))

sonuc = (sayi % 2 == 0)
print(f"{sayi} sayısı çift sayı mıdır? {sonuc}")
"""

# 3
"""
sayi = int(input("sayı: "))

sonuc = (sayi > 0)  # Pozitif
sonuc = (sayi < 0)  # Negatif
print(sonuc)
"""

# 4
"""
vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}")
"""

# 5

email = "info@sadikturan.com"
parola = "12345"

mail = input("email girin: ")
password = input("parola girin: ")

sonuc = (mail.lower().strip() == email), (password.strip() == parola)
print(sonuc)