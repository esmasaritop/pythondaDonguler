'''
1-100 arasında rastegele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
buldurmaya calısın.
** "random modülü" için "python random" seklinde arama yapın.
** kalan can sayısı * 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
üzerinden hesaplansın.
'''

import random
sayi= random.randint(1,100) #min 1 max 100 arasında random sayı üretir
sayac=0
hak= int(input('kaç hak kullanmak istersiniz? '))
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin: '))

    if sayi== tahmin:
        print(f'Tebrikler {sayac} defada bildiniz. Toplam puanınız {20*(hak-1)}')
        break
    elif sayi >tahmin:
        print('yukarı çık')
    else :
        print('aşağı in ')

        if hak==0:
            print(f'hakkınız bitti. Tutulan sayı: {sayi} ')




