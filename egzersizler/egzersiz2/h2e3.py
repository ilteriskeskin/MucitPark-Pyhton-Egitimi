while True:
    girdi1 = input("Üçgenin 1. kenar uzunluğunu giriniz :")
    girdi2 = input("Üçgenin 2. kenar uzunluğunu giriniz :")
    girdi3 = input("Üçgenin 3. kenar uzunluğunu giriniz :")
    print("\n")
    
    def hesapla(a,b,c):
        if a==b==c:
            print("bu EŞKENAR üçgendir")
            
        elif a==b or b==c or a==c: # OR = veya
            print("Bu İKİZKENAR üçgendir")
        
        else:
            print("Bu ÇEŞİTKENAR üçgendir")
            
    hesapla(girdi1,girdi2,girdi3)
