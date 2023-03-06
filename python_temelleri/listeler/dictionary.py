# dictionary = indekslenebilir, değiştirilebilir ama sıralanamaz.


sehirler = ['ısparta','samsun']
plakalar = [32,55]

"""
print(plakalar[0],sehirler[0])
print(plakalar[1],sehirler[1])

print(plakalar[sehirler.index('samsun')])
print(plakalar[sehirler.index('ısparta')])
"""


plakalar = {'ısparta': 32,'samsun': 55}

# print(plakalar['ısparta'])
# print(plakalar['samsun'])

plakalar['rize'] = 53
# plakalar['izmir'] = 36

# plakalar['izmir'] = 35 # 36 to 35
# print(plakalar)

ogrenciler = {
    100: {
        "ad":"Çınar",
        "soyad":"Turan",
        "yas":4,
        "notlar": [90,80,100]
    },
    101: {
        "ad":"Ada",
        "soyad":"Bilgi",
        "yas":10
    }
}

# sonuc = ogrenciler[100]["ad"]
sonuc = ogrenciler[101]["ad"]
sonuc = ogrenciler[101]["soyad"]

sonuc = ogrenciler[100]["notlar"][2]

sonuc = (ogrenciler[100]["notlar"][0] + ogrenciler[100]["notlar"][1] + ogrenciler[100]["notlar"][2]) / 3

print(sonuc)