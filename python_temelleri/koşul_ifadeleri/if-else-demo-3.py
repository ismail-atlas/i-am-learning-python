# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 
"""
isim = input("isim: ")
yas = int(input("yaş: "))
egitim = input("eğitim durumu: ")

if (yas >= 18):
    if (egitim == "lise") or (egitim == "üniversite") or (egitim == "önlisans"):
        print("Ehliyet alabilirsiniz.")
    else:
        print("eğitim durumunuz, ehliyet almaya uygun değil. En az lise olmalı.")
else:
    print("yaşınız, ehliyet almaya uygun değil. en az 18 yaşında olmalısınız.")
"""

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
"""
yazili1 = int(input("yazılı 1: "))
yazili2 = int(input("yazılı 2: "))
sözlü = int(input("sözlü: "))

ortalama = (yazili1 + yazili2 + sözlü) / 3

if 0 <= ortalama <= 24:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi sıfır.")
elif 25 <= ortalama <= 44:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi bir.")
elif 45 <= ortalama <= 54:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi iki.")
elif 55 <= ortalama <= 69:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi üç.")
elif 70 <= ortalama <= 84:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi dört.")
elif 85 <= ortalama <= 100:
    print(f"öğrencinin not ortalaması: {ortalama} ve not bilgisi beş.")
else:
    pass
"""

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı: ")
tarih = tarih.split("/")

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

if (gun <= 365):
    print("1. servis bakımı.")
elif (gun > 365) and (gun <= 365*2):
    print("2. servis bakımı.")
elif (gun >= 365*2) and (gun <= 365*3):
    print("3. servis bakımı.")
else:
    print("hatalı bilgi girdiniz.")