#print("selam")

#sayi = 1
#print(sayi)

#print(5**2)
#print(5%2)

#print(1&1)
#print("merhaba \n burası alt \t satır")

#liste = ["selam",1,'a',[1,2,3]]

#for i in range(len(liste)):
 #   print(liste[i])
#print("-"*30)
#for i in liste:
 #   print(i)
 
 #For döngüsü yardımı ile bir listeye 1 den 200 e kadar olan sayıları
 #yerleştirin. Daha sonra 1 ile 50 arası sayıların 3 e bölümünden kalanları,
 #50 ile 100 arasındaki sayıların 4 e bölümünden kalanları 100 ile 200 arasındaki
 #sayıların kareköklerini ekranda gösteren programı h4e7.py dosyasının içerisine yazınız.
 #Not: Bu işlemleri dizi içerisindeki elemanları kullanarak yapmalısınız.
 
#from math import sqrt
 
#sayilar = []
 
#for i in range(1,201):
#    sayilar.append(i)    
   
#n = len(sayilar)

#while n>0:
#    if sayilar[n-1]<50:
 #       print("{} sayısının  3 e bölümünden kalan = {}".format(sayilar[n-1],sayilar[n-1]%3))
  #  elif n>=50 and n<100:
  #      print("{} sayısının  4 e bölümünden kalan = {}".format(n,n%4))
   # elif n>=100 and n<200:
    #    print("{} sayısının karekökü {}".format(n,sqrt(n)))
        
   # n-=1
        
#for i in sayilar:
 #   if i <=50:
  #      print("{} sayısının  3 e bölümünden kalan = {}".format(i,i%3))
   # elif i>50 and i<100:
    #    print("{} sayısının  4 e bölümünden kalan = {}".format(i,i%4))
   # else:
    #    print("{} sayısının karekökü {}".format(i,sqrt(i)))
    

def fonksiyon_bir():
    print("Merhabalar bu benim ilk fonksiyonum")
    
    
    
def calisan(isim,soyisim,yas,sehir):

    
    print("İsim      : ",isim)
    print("Soyisim   : ",soyisim)
    print("yas       : ",yas)
    print("Sehir     : ",sehir)
    


#calisan("fikret","öztürk","","Rize")
#print("-"*30)
#calisan("selamet","samli","22","erzurum")



def selamla():
    print("Merhaba Zalim Dünya")
    
    
#selamla()


from math import sqrt

def karekok_al(sayi):
    sayi = sayi**1/2
    return sayi


def selamla2():
    return "Elvada Zalim Dünya"


#sayi = karekok_al(4)
#mesaj = selamla2()
#print(mesaj)
#print(sayi)


#def topla(a,b):
 #   toplam = a+b
 #   return toplam

#toplam_bir = topla(3,4)
#print("a degerimiz: ",toplam_bir,end=" ")
#toplam_iki = topla(10,10)
#print("b değerimiz: ",toplam_iki)

#toplam=topla(toplam_bir,toplam_iki)
#print(toplam)



#def araliktaki_sayilarin_toplami(baslangic,bitis):
 #   toplam = 0
  #  for i in range(baslangic,bitis):
   #     toplam = toplam+i
        
   # return toplam
    
#sayi = araliktaki_sayilarin_toplami(1,3)

#sayi*=2 #6
#toplam=araliktaki_sayilarin_toplami(sayi,sayi*2) #(6,12)
#print(toplam)


#def basamaklara_ayir(sayi):
#    basamaklar_listesi = []
#    while sayi>0:
#        basamak=sayi%10
#        sayi=sayi//10
#        basamaklar_listesi.append(basamak)
#    basamaklar_listesi.reverse()
    
#    return basamaklar_listesi
    
# a = basamaklara_ayir(123)

#for i in range(len(a)):
#    print ("{} indis deki sayı: {}".format(i,a[i]) )




#hesap makinesi
#toplama işlemi(1)
#çıkarma işlemi(2)
#...

#Yapmak istediğiniz işlemi seçiniz: 1
#sayi1 degerini girin
#sayi2 degerini girin
#topla (sayi1,sayi2)


def menuGoster():
    print("*"*15,"HESAP MAKINESI","*"*15)
    print("Toplama işlemi için (1)")
    print("Çıkarma işlemi için (2)")
    print("Çarpma işlemi için (3)")
    print("Bölme işlemi için (4)")
    print("Çıkış için (-1)")

def topla (sayi1,sayi2):
    toplam = sayi1+sayi2
    print("Toplam degerimiz: ",toplam)
    
def cikar (sayi1,sayi2):
    fark = sayi1-sayi2
    print("Fark degerimiz: ",fark)
    
def carp (sayi1,sayi2):
    carpim =sayi1*sayi2
    print("carpim degerimiz: ",carpim)
    
    
def bol(sayi1,sayi2):
    bolum = sayi1/sayi2
    print("Bölüm degerimiz: ",bolum)
    
#while True:
 #   menuGoster()
  #  secim=int(input("Lütfen bir seçim yapınız: "))
  #  if secim ==1:
  #      sayi1 = int(input("Sayı 1 Degerini giriniz:"))
  #      sayi2 = int(input("Sayı 2 Degerini giriniz:"))
  #      topla(sayi1,sayi2)
  #  elif secim == 2:
   #     sayi1 = int(input("Sayı 1 Degerini giriniz:"))
   #     sayi2 = int(input("Sayı 2 Degerini giriniz:"))
   #     cikar(sayi1,sayi2)
   # elif secim == 3:
   #     sayi1 = int(input("Sayı 1 Degerini giriniz:"))
   #     sayi2 = int(input("Sayı 2 Degerini giriniz:"))
   #     carp(sayi1,sayi2)
   # elif secim == 4:
   #     sayi1 = int(input("Sayı 1 Degerini giriniz:"))
   #     sayi2 = int(input("Sayı 2 Degerini giriniz:"))
   #     bol(sayi1,sayi2)
   # elif secim == -1:
   #     break
   # else:
    #    print("Hatalı giriş yaptınız.")
        

#print("birinci satır",end=" ")
#print("ikinci satır")



def geri_dondur():
    sayi1 = int(input("sayi 1 değerini giriniz: "))
    sayi2 = int(input("sayi 2 değerini giriniz: "))
    
    return sayi1,sayi2

a,b = geri_dondur()

print("a değerim: ",a)
print("b değerim: ",b )

a,b = b,a

print("a değerim: ",a)
print("b değerim: ",b )



