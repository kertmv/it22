#Kert Markus Vare
#02.11.2022
#harjutus10

#Koosta kood, mis väljastab õiged IP’d

import re

fh = open('i.txt')
for line in fh:
    if re.search('^[A-Z0-9]+[A-Z]{1}', line):
         print(line,end='')
         
         
#kuva korralikud paroolid
import re

fh = open('i.txt')
for line in fh:
    if re.search('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', line):
         print(line,end='')