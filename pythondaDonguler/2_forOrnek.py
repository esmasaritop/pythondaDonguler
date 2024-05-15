#Alıştırma1
sayilar= [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?
for sayi in sayilar:
    if sayi % 3== 0:
        print(sayi)

# 2- Sayilar listesindeki sayıların toplamı kaçtır?
toplam=0
for sayi in sayilar:
    toplam += sayi

print('toplam:',toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız.
for sayi in sayilar:
    if (sayi % 2 ==1):
        print(sayi,'>',sayi**2)

#Alıştırma2
sehirler=['kocaeli','istanbul','elazığ','izmir', 'rize',]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if len(sehir)<=5:
        print(sehir)

#Alıştırma3
urunler= [
    {'name': 'samsung a1', 'price':'3000'},
    {'name': 'samsung a2', 'price':'4000'},
    {'name': 'samsung a3', 'price':'5000'},
    {'name': 'samsung a4', 'price':'6000'}
]

# 5- Ürünlerin fiyatları toplamı nedir?
toplam=0
for urun in urunler:
    fiyat= int((urun['price']))
    toplam+=fiyat
print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])