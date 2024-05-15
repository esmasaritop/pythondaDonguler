'''name= 'esma sarıtop '

for letter in name:
    if letter=='a':
        break # donguden tamamen cıkıs yapar
    print(letter)

    for letter in name:
        if letter == 's':
            continue # donguden tamamen cıkmaz sadece dongu turunu iptal eder
        print(letter)'''

x=0
while x<5:
    x += 1
    if x==3 :  #3ü gorunce donguden cıkar
        break
    print(x)


print('hello ')
x=0
while x<5:
    x+=1
    if x==2 : #yalnızca 2 icin donguden cıkmıs olur 2 den sonra yine devam eder
        continue
    print(x)


# 1'den 100 e kadar çift sayıların toplamı
x=1
result=0
while x<= 100:
    x += 1
    if x%2==1:
        continue #erteler eger tek sayı ise yani esgecer
    result+=x
    x+=1
print(f'toplam: {result}')





