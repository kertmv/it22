#kert markus vare
#11.10.22
#harjutsu 3

#palindroom
def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")





#tundide ajad
algus= "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":") 
miniutid1 = int(hh1)*60+int(mm1)
hh2,mm2 = algus.split(":")
miniutid2 = int(hh2)*60+int(mm2)
minutid = minutid2-minutid1 #ajavahe
hh = minutid//60 #täisarvuline jagamine
mm = minutid%60 #jääk


print(f("Ajaline vahe on {hh}:{mm}")





#emaili kontroll true/false
email = input("sisesta emaili kontrollimiseks: ")
print("@" in email)


#vandumine = teksti asendamine
v = input("vannu siia 'kurat küll!' : ")
print(v.lower().replace("kurat","***"))



#korralik nimi
nimi = input("sisesta nimi: ")
puh_nimi =nimi.strip().capitalize
print("tere,", puh_nimi+"!")