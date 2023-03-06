isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998,2000,1998,1987]

# 1
isimler.append('Cenk')

# 2
isimler.insert(0,'Sena')

# 3
# isimler.remove('Yiğit')

# 4
# print(isimler.index('Yiğit'))

# 5
if "Beril" in isimler:
    print("Listenin bir elemanıdır.")

# 6
isimler.reverse()

# 7
isimler.sort()

# 8
yaslar.sort()
yaslar.reverse()

# 9
str = ["IPhone X","IPhone XR"]

# 10
sonuc = min(yaslar)
sonuc = max(yaslar)

# 11
print(yaslar.count(1998))

# 12
yaslar.clear()

# 13
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)

# sonuc = isimler
# sonuc = yaslar
# print(sonuc)