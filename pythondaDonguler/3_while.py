
# kosul tamamlanınca false değer duser
# islem bitince donguden cıkar


# 1-100 e kadar
x=1
while x <= 100 :
    print(x)
    x = x + 1

print('bitti.. ')

# cift ve tekleri ayırır
x=1
while x <= 100:
    if x % 2 ==1 :
        print(f'tek sayı:{x}')
    else:
        print(f'cift sayı: {x}')

    x = x + 1

print('bitti.. ')


name='' #False
while not name.strip() : #burdaki not name true demek aynı zamanda burdaki strip metodu
    # bosluk karakteri girince olusacak isimsiz hello mesajını engeller
    
    name=input('isminizi giriniz: ')

print(f'hello {name}')
#deger girmedikce bosluk karakterine esit olur
# name o zaman da false olmus olur
#ve bu da while dongusune girmiyor demek olur