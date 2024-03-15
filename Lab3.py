from tkinter import *
HEIGHT = 800
WIDTH = 1000
FONT = ("Arial Bold", 20)
TITLE = 'keygen'
def next_page():
    window.destroy()
    
window = Tk()
window.title(TITLE)
window.geometry(f'{WIDTH}x{HEIGHT}')
bg_image = PhotoImage(file="pic.png")
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

lbl = Label(window, text='Сгенерировать ключ?', font=FONT)
lbl.grid(column=0, row=0, padx=50, pady=680)
btn = Button(window, text='Да!', font=FONT, command=next_page)
btn.grid(column=1, row=0, padx=10, pady=680)

window.mainloop()

import random
SYMBOLS1 = 'Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M'
l1 = SYMBOLS1.split(",")
SYMBOLS2 = '1,2,3,4,5,6,7,8,9'
l2 = SYMBOLS2.split(",")
def get_key():
    s = []
    k = ''
    for i in range(4):
       m = random.choice (l1)
       s.append(m)
       m = random.choices (l2,k=3)
       s.append (''.join(m))
       s.append ("-")
    s.pop()
    for el in s:
        k += el
    return k

window = Tk()
window.title(TITLE)
window.geometry(f'{WIDTH}x{HEIGHT}')
bg_image = PhotoImage(file='pic.png')
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

key = get_key()
lbl_key = Label(window, text='Ваш ключ: ' + key, font=FONT)
lbl_key.grid(column=1, row=3, padx=30, pady=680)

window.mainloop()
