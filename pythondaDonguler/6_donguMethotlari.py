# range() liste olusturur. 'range(baslangıc, bitis,aralık) '
for item in range(3,40,2): # 3 ile 40 arasındaki sayıları 2ser atlayarak yazar
    print(item)

print(list(range(5,100,10)))


#enumerate
index=0
greeting= 'Hello There'

for letter in greeting:
    print(f'index: {index} letter: {greeting[index]} ')
    index+=1

greeting = 'Hello There'

for item in enumerate(greeting):
    print(item)
    print(f'index: {index} letter: {letter} ')

# zip listeleri  birleştirir
list1= [1,2,3,4]
list2= ['a','b','c','d']

print(list(zip(list1,list2)))


for item in zip(list1,list2):
    print(item) # yeni birleştirilmis liste 

for a,b in zip(list1,list2):
    print(a,b) # yeni liste
    print(a) #ilk listenin elemanlarını yazdırma
    print(b) # ikinci listenin elemanlarını yazdırmam


