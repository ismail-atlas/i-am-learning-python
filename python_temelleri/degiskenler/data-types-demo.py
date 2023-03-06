# Uygulama 1

"""
pi = 3.14
yaricap = int(input("yarıçap: "))

daireAlani = pi*(yaricap)**2
daireCevresi = 2*pi*(yaricap)

# print(daireCevresi)
# print(daireAlani)

result = "alan: " + str(daireAlani) + " çevre: " + str(daireCevresi)
print(result)
"""

# Uygulama 2

"""
km = int(input("km: "))
mil = km / 1.609344
print(mil)
"""
print("kaç km yol gittiniz?")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)
print(str(mesafeKm) + " km = " + str(mesafeMil) + " mil.")