sayilar=[1,3,5,7,9,12,19,21]

# 1- Sayıları while ile ekrana yazdırın.

i=0
while (i <len(sayilar)):
    print(sayilar[i])
    i+=1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki
#    tüm tek sayıları ekrana yazdırn.
baslangic= int(input('başlangıc: '))
bitis= int(input('bitis: '))
i=baslangic
while i < bitis:
    i += 1
    if i % 2 == 1:
     print(i)


# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100
while i>0:
    print(i)
    i-=1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
number = []
i=0
while i<5:
    sayi= int(input('sayı: '))
    number.append(sayi)
    i+=1
number.sort()
print(number)

# 5- Kullanıcıdan alacagınız sınırsız ürün bilgisisni urunler listesi icinde saklayan
#   ** ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name,price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler=[]

adet= int(input('kaç ürün eklemek istiyorsunuz: '))
i=0
while ( i< adet):
    name= input('ürün ismi: ')
    price= input('ürün fiyatı: ')
    urunler.append(
        {
            'name': name,
            'price': price
        }
    )
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")



