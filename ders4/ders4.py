# nesne = "Merhaba Dünya"
# sayi = 3.0
#
# print(nesne)
# print("Merhaba Dünya")
# print(type(nesne))
# print(type(sayi))
#
# veri = input("Bir şeyler giriniz: ")
#
# print(type(veri))
#
# tek_harf = ""
# print(type(tek_harf))

# karakterler = "12345"
#
# for i in karakterler:
#     print(i * 2)

# karakter_dizileri = "Python"
#
# print(karakter_dizileri[0])
# print(karakter_dizileri[1])
#
# sayilar = "1234"
#
# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
#
# print(int(sayilar[2]) * 2)
#
# # print(sayilar[len(sayilar)]) # print(sayilar[4])
# print(sayilar[len(sayilar) - 1])
#
# sayilar = "1234"
#
# print(sayilar[-1])
# print(sayilar[-2])
#
# for i in range(len(sayilar)):
#     print(sayilar[i])

# isim = input("İsminizi giriniz: ")
#
# for i in range(len(isim)):
#     print("İsminizin {}. harfi: {}".format(i + 1, isim[i]))

# site = "www.mucitpark.com"
# site1 = "www.istihza.com"
#
# print(site[4:13])
# print(site[0:3])
#
# for i in site, site1:
#     print("Site: ", i[4:-4])
#     print("Site: ", i[::-1])
#
# string = "Sana gül bahçesi aldım."
# for i in reversed(string):
#     print(i, end="")
#
# print(string[::-1])
#
# print(*reversed(string))
# print(*reversed(string), sep="")

# print(sorted("ali ilteriş"))

# meyve = "Elma"
#
# a = "s" + meyve
#
# print(a.lower())

# meyve = "Elma"
#
# print("e" + meyve[1:])

# sesli_harfler = "aeıioöuü"
# sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
#
# sesliler = ""
# sessizler = ""
#
# kelime = "istanbul"
#
# for i in kelime:
#     if i in sesli_harfler:
#         sesliler += i
#     else:
#         sessizler += i
#
# print("sesli harfler : ", sesliler)
# print("sessiz harfler: ", sessizler)
# print("sesli harfler alfabetik : ", sorted(sesliler))
# print("sessiz harfler alfabetik: ", sorted(sessizler))

# sayilar = [1,2,3,4,5,6]
#
# print(type(sayilar))
#
# sayilar[0] = 10
# print(sayilar)
# print("------------------")
#
# dizi = []
# sayi = 10
# dizi.append(sayi)
# print(dizi)

# ----------------------------------------------

# isimler = []
# soyisimler = []
# yaslar = []
#
# while True:
#
#     print("----------Hoşgeldiniz----------")
#     print("1- Kişi Ekle")
#     print("2- Kişileri Görüntüle")
#     print("3- Kişi Sil")
#     print("4- Çıkış")
#
#     secim = input("Seçiminizi Yapınız: ")
#
#     if secim == "1":
#         isim = input("İsminizi Giriniz: ")
#         soyisim = input("Soyisminizi Giriniz: ")
#         yas = int(input("Yaşınızı Giriniz: "))
#
#         isimler.append(isim)
#         soyisimler.append(soyisim)
#         yaslar.append(yas)
#
#     elif secim == "2":
#         print(isimler, soyisimler, yaslar)
#
#     elif secim == "3":
#         silinecek = int(input("Silmek istediğin kişinin numarasını giriniz: "))
#
#         del isimler[silinecek - 1]
#         del soyisimler[silinecek - 1]
#         del yaslar[silinecek - 1]
#
#     elif secim == "4":
#         print("Çıkış yapılıyor...")
#         break
#
#     else:
#         print("Hatalı giriş yapıldı.")


# import turtle

# kaplumbaga = turtle.Turtle()
# kaplumbaga.circle(150)
# turtle.getscreen()._root.mainloop()

# kaplumbaga = turtle.Turtle(shape = "turtle")
# kaplumbaga.circle(50)
# turtle.getscreen()._root.mainloop()

# import modul
#
# modul.ekranaYaz()
# modul.toplama(2,2)