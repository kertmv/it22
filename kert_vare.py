# kert vare
# 29.01.23
import random
from tkinter import *

aken = Tk()
aken.title('ulesanne 4.5 kt')
aken.geometry('180x150')
aken.maxsize(width=200, height=200)

# textbox ahha
laabel = Label(aken,text='mitu poialpoissi soovib ouna?')
laabel.grid(row=0,column=1, padx=2)

entry = Entry(aken)
entry.grid(row=1,column=1,columnspan=2,padx=1,pady=2)

laabel2 = Label(aken,text='poialpoiste ounad:')
laabel2.grid(row=3,column=1)

laabel3 = Label(aken,text='lumelembekese ounad:')
laabel3.grid(row=4,column=1)


#põhiline funktsioon
def naljakas():
    suvakasarv = 0 
    getentry = entry.get()
    for i in range(int(getentry)):
        randint = random.randint(1, 2)
        if randint == 1:
            suvakasarv += 1
        else:
            suvakasarv += 2
    laabel2.config(text=f'poialpoiste ounad: {suvakasarv}')
    laabel3.config(text=f'lumelembekese ounad: {14 - suvakasarv}')

buton = Button(aken, text='arvuta', command=naljakas)
buton.grid(row=2,column=1)

aken.mainloop()