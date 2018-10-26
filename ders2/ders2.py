# print("Bu programı kullanabilmek için +15 olmalısın.")
#
# yas = int(input("Yaşınızı giriniz: "))
#
# print("Yaşın: ", yas)
#
# if yas > 15:
#     print("Yaşınız kurtarıyor.")
#
# elif yas < 15:
#     print("Yaşınız kurtarmıyor.")
#
# else:
#     print("Yaşınız tam 15.")

# ---------------------------------------------------

# meyve = input("En sevdiğiniz meyveyi giriniz: ")
#
# if meyve == "elma":
#     print("Kırmızı mı, yeşil mi?")
#
# elif meyve == "armut":
#     print("Armutun iyisini....")
#
# else:
#     print("{} isimli meyveyi hiç yemedim.".format(meyve))

# ----------------------------------------------------

# sayi1 = int(input("Birinci sayıyı giriniz : "))
# sayi2 = int(input("İkinci sayıyı giriniz  : "))
#
# if sayi1 > sayi2:
#     print("Sayi1: ", sayi1, " > Sayi2: ", sayi2)
# elif sayi1 < sayi2:
#     print("Sayi1: ", sayi1, " < Sayi2: ", sayi2)
# else:
#     print("Sayılar birbirine eşittir.")

# ----------------------------------------------------

# 3 sayının en büyüğünü bulma
# sayi1 = int(input("Birinci sayıyı giriniz: "))
# sayi2 = int(input("İkinci sayıyı giriniz : "))
# sayi3 = int(input("Üçüncü sayıyı giriniz : "))
#
# enBuyuk = sayi1
#
# if sayi2 > enBuyuk:
#     enBuyuk = sayi2
#
# if sayi3 > enBuyuk:
#     enBuyuk = sayi3
#
# print(enBuyuk)

# ----------------------------------------------------

# kullaniciAdi = "ali"
# parola = "1234"
#
# ka = input("Kullanıcı adını gir: ")
# pr = input("Parolanı gir       : ")
#
# if ka == kullaniciAdi and pr == parola:
#     print("Giriş Başarılı!")
# else:
#     print("Kullanıcı adı veya parola yanlış")

# Alternatif (Tavsiye edilmez)
# if ka == kullaniciAdi:
#     print("Kullanıcı adınız doğru")
#     if pr == parola:
#         print("Parolanız doğru")
# else:
#     print("Kullanıcı adı yanlış")

# --------------------------------------------------------

#   Kullanıcıdan bir ay numarası (1-12) alınıp bu ay
# numarasının kaç gün olduğunu ekrana basan prograı yazın.

# ay = int(input("Bir ay numarası giriniz: "))
#
# if ay == 1 or ay == 3 or ay == 5 or ay == 7 or ay == 8 or ay == 10 or ay == 12:
#     print("Bu ay 31 gün var")
#
# elif ay == 4 or ay == 6 or ay == 9 or ay == 11:
#     print("Bu ay 30 gün var")
#
# else:
#     print("Bu ay şubat, 28 gün var")

# ---------------------------------------------------------

# print("-----------------------")
# print("1-Toplama\n"
#       "2-Çarpma\n"
#       "3-Bölme\n"
#       "4-Çıkarma")
# print("-----------------------")
# islem = int(input("Bir işlem seçiniz:"))
#
# sayi1 = int(input("Birinci sayıyı giriniz: "))
# sayi2 = int(input("İkinci sayıyı giriniz : "))
#
# if islem == 1:
#     toplam = sayi1 + sayi2
#     print("Toplam: ", toplam)
#
# elif islem == 2:
#     carpma = sayi1 * sayi2
#     print("Çarpım: ", carpma)
#
# elif islem == 3:
#     bolme = sayi1 / sayi2
#     print("Bölüm: ", bolme)
#
# elif islem == 4:
#     fark = sayi1 - sayi2
#     print("Fark: ", fark)
#
# else:
#     print("Aradığınız işlemi bulamadım.")

# ----------------------------------------------------

#   Bir Bisiklet kiralama firması müşterilerinden, yarım saate
# kadar olan kiralamalar için 5 TL ve bu süre aşımı
# sonrasındaki her bir dakika için 0.25 TL ücret talep
# etmektedir. Süre bilgisini kullanıcıdan dakika türünde
# alın ve ücreti ekrana bastırınız.

# sure = int(input("Otoparkı kullanacağınız süreyi girin: "))
#
# if sure <= 30 and sure > 0:
#     print("Ödemeniz gereken ücret 5TL'dir.")
#
# elif sure > 30:
#     fark = sure - 30
#     ucret = (fark * 0.25) + 5
#     print("Ödemeniz gereken ücret {}TL'dir.".format(ucret))
# else:
#     print("Hatalı giriş yaptınız!")

# ---------------------------------------------------------

# Kullanıcıdan kullanıcı adı ve parola iste. Kayıt olduktan sonra
# giriş yapmasını iste. Bilgiler doğru ise giriş yapsın değil ise
# hata versin.

# print("Kayıt olma ekranına hoş geldiniz.")
# kullaniciAdi = input("Kullanıcı adınızı giriniz: ")
# parola = input("Parolanızı giriniz       : ")
#
# print("Kayıt işlemi başarılı!")
# print("-------------------------")
# print("Giriş Yapınız.")
#
# girisKullaniciAdi = input("Kullanıcı adınızı giriniz: ")
# girisParola = input("Parolanızı giriniz       : ")
#
# if girisKullaniciAdi == kullaniciAdi and girisParola == parola:
#     print("Giriş başarılı :)")
# else:
#     print("Kullanıcı adı veya parola yanlış")

# ---------------------------------------------------------

# Modüllere Giriş

# import modul
#
# modul.yazi()

# import os
#
# print(os.name)
#
# if os.system("mkdir 'yeni'"):
#     print("Klasör oluştu")
#
# print(os.listdir("."))

# import math
# #
# sayi = 5
# #
# print(math.factorial(sayi))

# ---------------------------------

# Kullanıcıdan bir üçgenin üç kenarının
# boyutlarını alıp, üçgen çeşidini ekrana
# basan programı h2e3.py ismindeki
# dosyaya yazınız

# kenar1 = int(input("Birinci kenarı giriniz: "))
# kenar2 = int(input("İkinci kenarı giriniz : "))
# kenar3 = int(input("Üçüncü kenarı giriniz : "))
#
# if kenar1 == kenar2 == kenar3:
#     print("Eşkenar üçgendir.")
# elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
#     print("İkizkenar ügendir.")
# else:
#     print("Çeşitkenar üçgendir.")