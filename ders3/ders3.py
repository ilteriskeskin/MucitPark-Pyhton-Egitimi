# a = 1
# sayac = 1
#
# while a < 10:
#     print(a, "Merhaba")
#     a = a + 1 # a += 1
#     sayac = sayac + 1

# -----------------------------

# Sayı tahmin oyunu

# tutulan_sayi = 25
# hak = 3
#
# while hak>0:
#
#     print(hak, " tane hakkınız kaldı.")
#
#     tahmin = int(input("Bir tahmin giriniz: "))
#
#     if tahmin == tutulan_sayi:
#         print("Cevabın doğru")
#         break
#     else:
#         print("Cevabın yanlış")
#         hak = hak - 1  # hak -= 1

# ----------------------------------------

# sayac = 0
# toplam =0
#
# while sayac < 10:
#     toplam += sayac
#     print("Toplam Değerimiz: ",toplam)
#     sayac +=1

# ----------------------------------------

# while True:
#     print("1-Merhaba\n2-Çıkış")
#     secim = int(input("Menü seçiniz: "))
#
#     if secim == 1:
#         print("MERHABA")
#     elif secim == 2:
#         print("Çıkış yapılıyor...")
#         break
#     else:
#         print("Hatalı seçim tekrar seçiniz!")

# ------------------------------------------

# ejderiya = 2
#
# while ejderiya < 10:
#     yemek = input("Yemek türünü seçin (et: +3, ot: +1): ")
#     if yemek == 'et' or yemek == 'ET':
#         ejderiya += 3
#         print("Hayvanının yaşı {}".format(ejderiya))
#     elif yemek == 'ot' or yemek == 'Ot':
#         ejderiya += 1
#         print("Hayvanının yaşı {}".format(ejderiya))
#     else:
#         print("Hayvanın bu yiyecek ile beslenemez!")
#
# print("Hayvanın artık büyüdü.")

# ------------------------------------------

# tr_harfler = "şçöğüİı"
# sayilar = "123456"
#
# for harf in tr_harfler:
#     print(harf)
#
# for sayi in sayilar:
#     print(sayi)

# for değişken_Adi in değişken:
#   yaplicak_işlem
#

# ----------------------------------------------------

# tr_harfler = "şçöğüİı"
#
# parola = input("Parolanızı giriniz: ")
#
# for i in parola:
#     if i in tr_harfler:
#         print("Parolanızda Türkçe Karakter kullanamazsınız!")

# -----------------------------------------------------

# isim = "Ali Keskin"
#
# for i in isim:
#     print("i = ", i)

# ------------------------------------------------------

# for i in range(12, 0, -2):
#     print("i:", i)

# ------------------------------------------------------

# isim = "Ali İlteriş Keskin"
#
# for i in range(1, 11):
#     print(i, ":", isim)

# ------------------------------------------------------

# Kullanıcıdan başlangıç ve bitiş değerlerini alıp
# ekrana toplamını basan programı yazınız.

# baslangic = int(input("Başlangıç değerini giriniz: "))
# bitis = int(input("Bitiş değerini giriniz    : "))
#
# toplam = 0
#
# # range(başlangıç, bitiş, artış miktarı)
#
# for i in range(baslangic, bitis):
#     toplam = toplam + i # toplam += i
#
# print("Toplam: ", toplam)

# ------------------------------------------------------------