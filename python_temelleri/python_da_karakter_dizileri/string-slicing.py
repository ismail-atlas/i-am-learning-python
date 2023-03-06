ad = 'İsmail'
soyad = 'Uludağ'
yas = '23'

msj = 'Benim adım ' + ad + ' ve soyadım ' + soyad + '. Yaşım ise ' + yas + '.'

print(len(msj))

print(msj[0])   # B
print(msj[1])   # e
print(msj[6])   # a
print(msj[-1])  # .

print(msj[0:5])
print(msj[6:20])
print(msj[:20])
print(msj[10:])

print(msj[-10:-1])
print(msj[0:40])

print(msj[0:40:2]) # adım sayısını belirliyoruz. 2 adım git gibi
print(msj[0:40:3])
print(msj[::1])
print(msj[::-1]) # sağdan sola doğru yazılır.

