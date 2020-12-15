gun = input("Kiralamak istediğiniz gün sayısınız yazınız: ")
fiyat = input("Kiralama bedelini yazınız: ")



def hesapla(kiragun,kirafiyat):
    if int(kiragun) <= 7:
        fiyat1 = int(kiragun) * int(kirafiyat)
        fiyat1 = (fiyat1)
        print(fiyat1)
    elif int(kiragun) > 7:
        normalfiyat = int(kiragun) * int(kirafiyat)
        fark = (int(kirafiyat)*19)/100
        toplam = normalfiyat + fark
        print("\n Toplam kiralama beledi {} Tl dir.\n 7 günü geçen kiralamalarda %19 iskonto uygulanmaktadır.".format(toplam))
       
        
hesapla(gun,fiyat)
        
