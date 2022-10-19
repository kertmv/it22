#kert markus vare
#17.10.2022
#harjutus04
import random

#pank
konto = 10000
intress = 0.05
periood = 5

for i in range(1,periood+1):
    print(f"{i} {konto} {round(konto*intress}{konto+konto*intress}")
    konto = konto+konto*intress
print(f"Konto seis: {round(konto,2)}")
print(f"Kasum  {round(konto,2)}")
    


print()
"""
#arvutimäng

while loop==1:
    suvarv = random.randint(1,10)
    print(suvarv) #testimiseks
    for i in range(3):
        valik = int(input("vali arv 1-10: "))
        if valik == suvarv:
            print("WINNER!")
            skoor+=1
            break
        else:
            print("vale")
    loop = int(input("veel







#viisikud












#pisike korrutustabel

arv = 5
for i in range(1,11):
summa = arv * i
print(f"{arv}x{i}={summa}")








#"paaris ja paaritu

for i in range(1,11):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")
        
        

 
 




#loto
for i in range(5):
   suv = random.randint(0,9)
   print(suv, end="")
   
   
   
   

"""
#tsükkel
arv = 5
for i in range(5):
    print("* " * arv)
    arv -= 1


nr = 5
for i in range(nr):
    print("* " * nr)




#jalka
vanus = 17
sugu = "m"

if vanus>=16 and vanus<=18 and sugu=="m":
    print("sobib meeskonda")
else:
    print("ei sobi")
  








#Myyk
hind = 9
if hind<=10:
    ale = 0.1
else:
    ale = 0.2
summa = hind-hind*ale
    
print(f"summa: {hind-hind*ale}")








#juubel
vanus = "09.03.2006"
aasta = 2022
p,k,a = vanus.split(".")

tema_vanus = aasta int(a)

if tema_vanus%5==0:
    print("juubel")
    else:
        print("ei ole juubel")



#matemaatika
nr1,nr2 = 8,6
tehe = input("Vali tehe (* / + -):")

if tehe=="*":
    vastus = nr1 * nr2
elif tehe=="/":
    vastus = nr1 /nr


else:
    vastus = "n/a"
    
 


print(f"{nr1}{tehe}{nr2}={vastus}")




#kas tegemist on ruuduga?
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
if a==b:
    print(f"{a} {b} moodustavad ruudu")
else:
        print(f"{a} ja {b} moodustavad ristküliku")
"""
        