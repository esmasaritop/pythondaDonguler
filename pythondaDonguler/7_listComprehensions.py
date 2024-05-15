# for ve while dongusune alternatif olarak kullanılabilinecek bir yontemdir
# kullanımı >>>  (işleyecegin işlem) for (içinde tutacagın yer adı) in (alacagın yer )

for x in range(10):
    print(x)

# 0dan 10 a kadar yazdırdı
numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)

#10a kadar olan sayıları yazdırma
numbers=[ x for x in range(10)]
print(numbers)

# 10a kadar olan 3ün katı sayıların karesini alma
numbers= [ x*x for x in range(10)]
print(numbers)
numbers= [ x*x for x in range(10) if x%3==0 ]
print(numbers)

#bir kelimenin harflerini listeye cevirme
myString = 'Hello'
myList= []
for letter in myString:
    myList.append(letter)
print(myList)

#yas hesaplaması
years=[1973,1981,2004,2013]
age=[2024-year for year in years]
print(age)

result= [x if x%2==0 else 'Tek' for x in range(1,10)]
print(result)


result= []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers= [(x,y) for x in range(3) for y in (7,5)]
print(numbers)
