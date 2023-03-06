opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka")

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values():      # values = bütün bilgileri verir.
#     print(x)

# for x,y in opelObj.items():
#     print(x,y)

# sonuc = "markaa" in opelObj     # liste içinde varsa True, yoksa False cevabını verir.

# sonuc = len(opelObj)
# opelObj["renk"] = "kırmızı"
# opelObj.pop("renk")               # istediğn şeyi siler.
# opelObj.popitem()                 # sondakini siler.  

# del opelObj["marka"]                # istediğin şeyi siler.
# del opelObj                         # NameError: name 'opelObj' is not defined

# opelObj.clear()                       # içindeki herşeyi siler.

obj = opelObj.copy()  # opelObj değişmez. Sadece obj değişir.
# obj = opelObj         # referans  # bunda da ikiside değişir.   

obj["marka"] = "mazda"

opelObj.update({
    "marka": "BMW",
    "renk": "mavi"
})                      # uptade = günceller ve üstüne eklemeler yapar.

# print(sonuc)
print(obj)
print(opelObj)