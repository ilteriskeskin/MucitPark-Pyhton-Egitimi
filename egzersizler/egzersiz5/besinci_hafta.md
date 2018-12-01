# Besinci Hafta Egzersizleri

NOT: Fonksiyonlarda kullanınlan parametreler aksi belirtilmedik taktirde kullanıcıdan alınacaktır.

1) Parametre olarak isim, soyisim, yas gibi değişkenlerini alan bu girdileri ekranda basan programı bir fonksiyon yardımı ile yazınız h5e1.py dosyasının içerisine yazınız.

Örnek fonksiyon kullanımı:
```
    ekranaBas(isim, soyisim, yas)
```

2) Paramete olarak aldığı sayının faktöriyelini hesaplayan ve bu değeri geriye döndüren bir fonksiyonu oluşturun ve bu programı h5e2.py dosyasının içerisine yazınız.
    * NOT: math kütüphanesi kullanımına izin yoktur.
3) Parametre olarak kullanıcından başlangıç ve bitiş değerlerini alan ve bu aralıktaki sayılardan tek olanlarının kareleri toplamını geriye döndüren bir fonksiyon oluşturun ve bu programı h5e3.py dosyasının içerisine yazınız.

Örnek Fonksiyon kullanımı:
```
hesapla(baslangic,bitis) 
#parametre olarak rakam girilmeyecektir.
```

4) 
* Parametre olarak aldığı öğrenci numarasının rakamları toplamını hesaplayan ve geriyen döndüren "rakamlarToplami()" isimli fonksiyon oluşturun.
* Geriye döndürülen değeri numaraOrtalamasi() adlı fonksiyona parametre olarak gönderin. numaraOrtalamasi() isimli fonksiyon ortalamayı hesaplayıp bu değeri döndürsün.

    Yukarıdaki koşulu sağlayan programı h5e4.py dosyasının içersine yazınız.

5) İçerisinde rastgele sayılar barındıran 10 elemanlı bir listeyi random() modülü yardımı ile oluşturun. Kendisine parametre olarak bu listeyi alan:
    * buyuktenKucuge() isimli fonksiyon oluşturun, bu fonksiyon listedeki elemanları büyükten küçüğe sıralayıp ekranda göstersin.
    * kucuktenBuyuge() isimli bir fonksiyon daha oluşturun, bu fonksiyon listedeki elemanları küçükten büyüğe sıralayıp ekranda göstersin.

    Yukarıdaki koşulu sağlayan programı h5e5.py dosyasının içersine yazınız.

6) Parametre olarak aldığı sayı mükemmel sayı ise ekrana "... sayısı mükemmel bir sayıdır." mükemmel sayı değil ise ekrana "... sayısı mükemmel sayı değildir." yazdıran bir fonksiyon oluşturun ve bunu h5e6.py dosyasının içerisine yazınız.

```
Mükemmel sayılar pozitif tam bölenleri toplamı kendisine eşit olan tam sayılardır. 6 bir mükemmel sayıdır çünkü 6 nın tam bölenleri olan 1, 2 ve 3 sayısının toplamı 6 dır.

6,28,496 Mükemmel sayılardır.

```

7) Kullanıcılar seçim hakkı sunan, ve taban dönüşüm işlemi gerçekleştiren bir programı fonksiyon yardımı ile yapınız.

    Program işleyişi:
    ```
    ********** TABAN DÖNÜŞTÜRÜCÜ **********
    1) 10(ecimal) -> 2(binary)
    2) 2(binary) -> 10(decimal)
    Lütfen yapmak istediğiniz işlemi seçiniz: # 1 girdiğimizi varsayıyorum. 
    Lütfen decimal(onlu) bir sayı girin: 10
    Girdiğiniz sayının decimal(onlu) degeri: 10 binary(ikilik) değeri :1010
    ```
    Eğer işlem numarası olarak 2 girilirse kullanıcıdan ikilik tabanda aldığı değeri onluk taban çeverecek.

    Birinci seçenek için decimal_to_binary(), ikinci seçenek için binary_to_decimal() isimli fonksiyon oluşturun.

    Bu programı h5.e7.py dosyası içersine yazınız.