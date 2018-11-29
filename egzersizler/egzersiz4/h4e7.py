from math import sqrt

liste =[]

for i in range(1,201):
    liste.append(i)
    
    
for i in liste:
    if i<=50:
        print("{} sayısının 3 bölümünden kalan = {} ".format(i,i%3))
    elif i>50 and i<=100:
        print("{} sayısının 4 bölümünden kalan = {} ".format(i,i%4))
    elif i>100 and i<=200:
        print("{} sayısının karekökü = {} ".format(i,sqrt(i)))
