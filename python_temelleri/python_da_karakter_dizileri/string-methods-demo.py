website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1
"""
h = ' Hello World '
sonuc = h.strip()
"""

# 2
"""
w = 'www.sadikturan.com'
sonuc = w.index('sadikturan')
sonuc = w[4:-4]
"""
# w = 'www.sadikturan.com'
# s = w.strip('w.com')
# print(s)

# 3
sonuc = kursAdi.lower()

# 4
sonuc = website.count('a')
sonuc = kursAdi.count('a')

# 5
sonuc = website.startswith('www')
sonuc = website.endswith('com')

# 6
sonuc = website.index('.com')
sonuc = website.find('.com')

# 7
sonuc = kursAdi.isalpha()
sonuc = "1231234".isdigit()
sonuc = "asfaf".isalpha()

# 8
c = "Contens".center(50,'*')
c = "Contens".ljust(50,'*')
c = "Contens".rjust(50,'*')
print(c)

# 9
sonuc = kursAdi.replace(' ','-')

# 10
sonuc = 'Hello World'.replace('World', 'There')

# 11
kursAdi = kursAdi.lower().replace(':','')
sonuc = kursAdi.split()
print(sonuc)