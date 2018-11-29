sayilar = []

sayac = 1
while(sayac<=10):
    sayi = int(input("sayiyi giriniz: "))
    sayilar.append(sayi)
    sayac+=1
    
n = len(sayilar)
    
for i in range(n): # sayilar dizi içerisindeki eleman sayısı kadar dön
    for j in range(n-i-1):
        if sayilar[j] > sayilar[j+1] : 
                sayilar[j], sayilar[j+1] = sayilar[j+1], sayilar[j]

print("Küçükten Büyüğe Sıralama: ")
for i in sayilar:
    print(i,end=" ")
    
for i in range(n): # sayilar dizi içerisindeki eleman sayısı kadar dön
    for j in range(n-i-1):
        if sayilar[j] < sayilar[j+1] : 
                sayilar[j], sayilar[j+1] = sayilar[j+1], sayilar[j]

print("\nBüyükten Küçüğe Sıralama: ")
      
for i in sayilar:
    print(i,end=" ")