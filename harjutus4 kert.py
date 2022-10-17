#kert markus vare
#17.10.2022
#harjutus04


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
        