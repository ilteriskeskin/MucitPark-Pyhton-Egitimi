liste = []

for i in range(0,13):
    a = int(input("sayı giriniz: "))
    liste.append(a)
    
for i in range(0,12,2):
    liste[i], liste[i+1] = liste[i+1],liste[i]
 
for i in liste:
    print(i,end=" ")