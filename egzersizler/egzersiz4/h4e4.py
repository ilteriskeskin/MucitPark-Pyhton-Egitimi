liste = []
sayac = 0

while True:
    sayi = int(input("Lütfen bir sayı giriniz: "))
    liste.append(sayi)
    
    for i in liste:
       if sayi == i:
            sayac+=1
    print("{} sayısı {} kez girilmiştir.".format(i,sayac))
    sayac = 0