# numbers listesi icinden num icine at ve her for donusunde yazdır
numbers=[1,2,3,4,5]
for num in numbers:
    print(num)

#ornek2
#sıra sıra esma emre ve haktan icin my name is... yazdırır
names=['esma','emre','haktan']
for name in names:
    print(f'my name is {name} ')

#ornek3
#tüm harfleri tek tek yazdırır
name='esma sarıtop'
for n in name:
    print(n)

#ornek4
#tuple icindeki değerleri yazdırır
tuple= ((1,2),(3,4),(4,3))
for a,b in tuple:
    print(a,b)

#ornek5.1
#k1,k2,k3 yazdırı
d= {'k1':1, 'k2':2, 'k3':3 }
for item in d:
    print(item)
    
#ornek5.2
#hem key hem value degerlerini yazdırır
for key,value, in d.items():
    print(key)
    print(value)