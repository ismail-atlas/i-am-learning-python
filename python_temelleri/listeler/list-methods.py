sayilar = [1,5,8,5,9,3,42,123,2,4,7]
harfler = ['a','b','c','a','s','y']

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

# ekleme
sayilar.append(10) # listenin sonuna 10 sayısını ekler.
sayilar.insert(3,5) # istediğin herhangi bir yere 5 sayisini ekler.
sayilar.insert(-1,50)
sayilar.insert(len(sayilar),350) # listenin sonuna ekler.

# silme
sayilar.pop() # listenin sonundan siler.
sayilar.pop(3) # istediğin herhangi bir konumdan siler.
sayilar.remove(42) # istediğin sayıyı siler.
harfler.remove('y')

# sıralama
sayilar.sort() # küçükten büyüğe doğru sıralar.
harfler.sort() # alfabetik sıralar.
sayilar.reverse() # büyükten küçüğe doğru sıralar.

# print(sayilar.count(5)) # belirtilen sayıdan liste içinde kaç tane olduğunu söyler. 
# print(harfler.count('a'))

print(sayilar.index(2)) # belirtilen sayının kaçınçı sırada olduğunu söyler.

sayilar.clear() # bütün elemanları siler.

sonuc = harfler
sonuc = sayilar
print(sonuc)