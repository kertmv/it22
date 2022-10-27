#kert markus vare
#27.10.22
#harjutus06

minu_fail = open("s6pru_l6ustaraamatus.txt, "r")
reformikad = 0
kesikud = 0

for in minu_fail.readlines():
    enimi,pnimi,er,palk = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesikud+=1
    if er not in erakonnad:
        erakonnad.append(er)
        
print(f"reformikaid kokku:{reformikad}")
print(f"kesikuid kokku: {kesikud}")
print(f"erakondi kokku: {len(erakonnad)}")


minu_fail.close



