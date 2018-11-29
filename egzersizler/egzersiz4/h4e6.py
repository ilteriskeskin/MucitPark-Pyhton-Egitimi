sayi_basamaklari= []
sayi = int(input("Lütfen Üç basamaklı bir sayı giriniz: "))

for i in str(sayi):
    sayi_basamaklari.append(i)
    
sayi_basamaklari.reverse()

print("Girilen sayı : {} tersi: ".format(sayi),end=" ")
for i in sayi_basamaklari:
    print(i,end="")
print()
    
for i in range(0,3):
    print("{}. indisteki sayi :{}".format(i,sayi_basamaklari[i]))
