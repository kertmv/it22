#kert markus vare
#11-10-22
# harjutus 02
import math

#kütusekulu arvutamine
km = 400
L = 26
v = 1/km/100)
print(v)





#Arvusüsteemid

b = int(input("sisesta täisarv: "))
print("2ndsysteemis:", bin(b))
print("16ndsysteemis:", hex(b))





#Ajateenistus
aeg = input("Sisesta minutid: ")
tunnid = aeg//60 #täisarvuline jagamine
minutid = aeg % 60 #jääk
print("vastus:",minutid,":"tunnid)






#hypotenuus
a,b = 16,9
c =round(math.sqrt(pow(a,2) + b**2),2)
print("Kolmunrga hüpo on:",c)






#rulluisutaja
kiirus = 29.9
aeg = 24
vastus = kiirus/60*aeg
print("Sportlane jõuab", kaugus,"km")





#pitsa
#4.73

#toote hind
kogus = 3
hind = 12.90
jootraha = 10
summa = (hind+hind*tip)/kogus
print("iga tyyp maksab",summa,"eurot")





#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus,"toote summa om ",summa, "eurot")

#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a + b + c
print("kolmnurga ümbermõõt on: ", p)




  
  