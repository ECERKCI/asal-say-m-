sayi = int(input('sayı: '))
asalMi= True

if sayi== 1:
    asalMi= False
for i in range (2, sayi):
    if (sayi % i==0):
        asalMi = False
        break
if asalMi:
    print('sayi asaldir.')   
else :
    print('sayi asal değildir.')    
