#kert markus vare
#01.11.22
#harjutus09

import locale
import datetime

#Tekita tänane kuupäev ning esita kujul 16. June 2016


aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

#Kuva eestistatud kuupäev kujul 16. juuni 2016
locale.setlocale(locale.LC_ALL, "et_EE")
print(aeg.strftime("%d. %B %Y"))




#Eralda iskukoodist sünnikuupäev ja leia isiku vanus
ik="38011064711"
sp = datetime.date(int("19"+ik[1:3]),int(ik[3:5]),int(ik[5:7]))
print(aeg.year-sp.year)