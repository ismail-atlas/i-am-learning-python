meyveler = {"elma","kiraz","kavun","üzüm"}
sebzeler = {"bezelye","soğan"}

# sonuc = meyveler[0]     # TypeError: 'set' object is not subscriptable
sonuc = "elma" in meyveler
meyveler.add("karpuz")
meyveler.update(["vişne","muz"])    # Birden fazla ekleme yapar.

sonuc = len(meyveler)
# meyveler.remove("karpuz")       # belirttiğin şeyi siler.
# meyveler.remove("karpuzz")      # KeyError: 'karpuzz'
# meyveler.discard("karpuz")      # belirttiğin şeyi siler.
meyveler.discard("karpuzz")       # hata mesaji vermez ve belirttiğin şeyi de silmez.

sonuc = meyveler.pop()  # rastgele şeyleri siler.

# meyveler.clear()         # listedeki bütün elemanları siler.

sonuc = meyveler.union(sebzeler)    # iki listeyi de birleştirir.

# print(type(meyveler))

"""
for x in meyveler:
    print(x)
"""

print(sonuc)
