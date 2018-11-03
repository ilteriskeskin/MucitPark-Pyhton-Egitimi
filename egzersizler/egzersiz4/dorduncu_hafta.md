# Üçüncü Hafta Egzersizler

1) Kullanıcıdan 3 kez aldığı isim ve yaş bilgisini bir liste içerisinde tutan ve bu listeyi ekranda gösteren programı h4e1.py dosyasının içerisine yazınız.


    ``` 
    replace() split(), rsplit(), splitlines(),lower(), upper() ,  
    islower(), isupper() ,endswith(), startswith(),capitalize(),   
    title(),swapcase(),casefold(),strip(), lstrip(), rstrip(),join(),
    count(),index(), rindex(),find, rfind(),center()
    ```
 2)   Yukarıda verilen methodları bir liste oluşturup deneyin.    Seçtiğiniz 5 fonksiyon için açıklama yaparak ekrana basan  programı h4e2.py dosyasının içerisinde yazınız.

Örnek Çıktı:

```
        replace() : Karakter dizisi içerisindeki  karakterleri değiştirmeye yarar.

        replace()' den önce: selamet sonra: Selamet

```
Örnek çıktıda kullanılan replace methodu kullanımı:
    
```
        s = "selamet"
        print(s) #selamet
        s.replace("s","S")
        print(s) # Selamet
```

3) Kullanıcıdan alınan 13 sayıyı bir liste içerinde tutan ve bu liste içerisindeki sayıların tek ve çift olanlarının yerlerini değiştirerek ekranda öncesi ve sonrası şeklinde gösteren programı h4e3.py dosyasının yazınız. 
```
    [1,2,3,4,5,6] -> [2,1,4,3,6,5] şekline çevirilmeli
```

4) Kullanınıcıdan istediğiniz kadar sayı alın ve bu sayıları kullanıcının kaç kez girdiğini ekranda gösteren programı h4e4.py dosyasının içerisine yazınız.
Örnek çıktı:
```
    1 sayısı 2 kez girilmiştir.
    2 sayısı 1 kez girilmiştir.
    ...
```


5) Kullanıcının alınan 10 sayıyı bir liste içerisinde tutunuz. Daha sonra bu liste içerisindeki elemanları küçükten büyüğe ve büyükten küçüğe sıralayıp ekranda gösteren programı h4e5.py dosyasının içerisine yazınız.

6) Kullanıcıdan aldığı 3 basamaklı sayının tersi bir liste içerisinde tutun ve aşağıdaki gibi çıktıyı bulan programı h4e6.py dosyasının içerisine yazınız

```
    Girilen sayı : 123  tersi :321
    0. indisteki sayı :3
    1. indisteki sayı :2
    2. indisteki sayı :1
```

7) For döngüsü yardımı ile bir listeye 1 den 200 e kadar olan sayıları yerleştirin. Daha sonra 1 ile 50 arası sayıların 3 e bölümünden kalanları, 50 ile 100 arasındaki sayıların 4 e bölümünden kalanları 100 ile 200 arasındaki sayıların kareköklerini ekranda gösteren programı h4e7.py dosyasının içerisine yazınız. Not: Bu işlemleri dizi içerisindeki elemanları kullanarak yapmalısınız.

    Çıktı örneği:
    ```
    1-50 arasındaki sayıların 3 bölümünden kalan:
    1 'in 3 e bölümünden kalan = 1
    ...
    50 'in 3 e bölümünden kalan = 2
    -------------------------------------------
    50-100 arasındaki sayıların 4 e bölümünden kalan:
    51'in 4 e bölümünden kalan = 3
    ...
    100'ün 4 e bölümünden kalan = 0
    -------------------------------------------
    100-200 arasındaki sayıların karekökleri :
    100'ün karekökü = 10
    ...
    200'ün karekökü = 14.14
    ```
