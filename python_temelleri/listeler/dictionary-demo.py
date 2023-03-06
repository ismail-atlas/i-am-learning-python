# 1
urunler = {
        '1': {'ad': 'samsung', 'fiyat': '1000'}, 
        '2': {'ad': 'iphone', 'fiyat': '2000'}, 
        '3': {'ad': 'laptop', 'fiyat': '3000'}
}

"""
id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad":ad,
    "fiyat":fiyat
}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad":ad,
    "fiyat":fiyat
}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad":ad,
    "fiyat":fiyat
}
"""

id = input("aramak istediğiniz ürün id: ")
urun = urunler[id]

print(f"id: {id} ürün adı: {urun['ad']} ürün fiyatı: {urun['fiyat']}")
# print(urunler)